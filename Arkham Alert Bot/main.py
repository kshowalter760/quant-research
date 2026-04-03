import time
from pprint import pprint

from alerts import (
    build_dex_stablecoin_alert,
    build_exchange_outflow_alert,
    normalize_transfer,
)
from arkham_client import ArkhamClient
from config import settings
from discord_notifier import DiscordNotifier
from state_manager import FlowTracker, StateManager, detect_repeated_flow
from utils import first_item, save_json

state = StateManager(settings.SEEN_ALERTS_PATH)
flow_tracker = FlowTracker()


def run_once() -> None:
    if not settings.ARKHAM_API_KEY:
        raise ValueError("Missing ARKHAM_API_KEY environment variable.")

    client = ArkhamClient(
        api_key=settings.ARKHAM_API_KEY,
        base_url=settings.ARKHAM_BASE_URL,
    )
    notifier = DiscordNotifier(settings.DISCORD_WEBHOOK_URL)


    print("Fetching live transfer data from Arkham...")

    raw_data = client.get_recent_transfers(
        time_last="24h",
        limit=200,
    )

    save_json(settings.RAW_OUTPUT_PATH, raw_data)
    print(f"Saved raw response to: {settings.RAW_OUTPUT_PATH}")

    if isinstance(raw_data, dict):
        transfers = raw_data.get("transfers", [])
        if not transfers:
            for value in raw_data.values():
                if isinstance(value, list):
                    transfers = value
                    break
    elif isinstance(raw_data, list):
        transfers = raw_data
    else:
        transfers = []

    sample = first_item(transfers)
    if not sample:
        print("No transfers returned.")
        print("Raw response:")
        pprint(raw_data)
        return

    print("\nTop-level keys from first transfer:")
    pprint(list(sample.keys()))

    print("\nFirst raw transfer sample:")
    pprint(sample)

    normalized_sample = normalize_transfer(sample)
    print("\nFirst normalized transfer sample:")
    pprint(normalized_sample)

    print(f"\nProcessing {len(transfers)} transfers...")

    alerts_sent = 0
    processed = 0

    for raw_tx in transfers:
        tx = normalize_transfer(raw_tx)

        usd_value = tx.get("usd_value")
        if usd_value is None:
            continue

        try:
            usd_value = float(usd_value)
        except (TypeError, ValueError):
            continue

        if usd_value < settings.MIN_GLOBAL_USD:
            continue

        processed += 1

        print(
            "TX CHECK | "
            f"from={tx.get('from_name')} | "
            f"from_type={tx.get('from_entity_type')} | "
            f"to={tx.get('to_name')} | "
            f"to_type={tx.get('to_entity_type')} | "
            f"token={tx.get('token_symbol')} | "
            f"usd={tx.get('usd_value')}"
        )

        key, flows = flow_tracker.add(tx)

        if flows and detect_repeated_flow(flows):
            pattern_id = f"pattern:{key[0]}:{key[1]}"

            if not state.has_seen(pattern_id):
                usd_values = [
                    float(flow["usd"])
                    for flow in flows
                    if flow.get("usd") is not None
                ]
                avg_usd = sum(usd_values) / len(usd_values) if usd_values else 0

                message = (
                    f"🚨 **Repeated Flow Detected**\n"
                    f"Protocol: `{key[0]}`\n"
                    f"Token: `{key[1]}`\n"
                    f"Count: `{len(usd_values)}`\n"
                    f"Avg USD: `${avg_usd:,.2f}`\n"
                )

                print(f"Sending pattern alert: {pattern_id}")
                print(message)
                notifier.send_message(message)
                state.mark_seen(pattern_id)
                alerts_sent += 1

        alert = build_exchange_outflow_alert(
            tx,
            min_usd_value=settings.MIN_USD_VALUE,
        )

        if not alert:
            alert = build_dex_stablecoin_alert(
                tx,
                min_usd_value=settings.MIN_USD_VALUE,
            )

        if not alert:
            continue

        if state.has_seen(alert["id"]):
            print(f"Skipping duplicate alert: {alert['id']}")
            continue

        print(f"Sending alert: {alert['id']}")
        print(alert["message"])
        notifier.send_message(alert["message"])
        state.mark_seen(alert["id"])
        alerts_sent += 1

    print("\nDone.")
    print(f"Processed (after filter): {processed}")
    print(f"Alerts sent: {alerts_sent}")


def main() -> None:
    print("Starting Arkham Alert Bot...")

    while True:
        try:
            run_once()
        except Exception as e:
            print(f"Error: {e}")

        print("Sleeping for 60 seconds...\n")
        time.sleep(60)


if __name__ == "__main__":
    main()
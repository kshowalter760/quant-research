from typing import Any, Dict, Optional


def normalize_transfer(raw: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize Arkham transfer payloads into a cleaner internal schema.
    Supports both:
    - older style: toAddresses = [{address: {...}, value: ...}]
    - newer style: toAddress = {...}
    """

    from_obj = raw.get("fromAddress") or {}
    from_entity = from_obj.get("arkhamEntity") or {}
    from_label = from_obj.get("arkhamLabel") or {}

    to_obj = {}
    to_entity = {}
    to_label = {}
    amount = None

    if raw.get("toAddress"):
        to_obj = raw.get("toAddress") or {}
        to_entity = to_obj.get("arkhamEntity") or {}
        to_label = to_obj.get("arkhamLabel") or {}
        amount = raw.get("value") or raw.get("unitValue")
    else:
        to_addresses = raw.get("toAddresses") or []
        first_to = to_addresses[0] if to_addresses else {}
        to_obj = first_to.get("address") or {}
        to_entity = to_obj.get("arkhamEntity") or {}
        to_label = to_obj.get("arkhamLabel") or {}
        amount = first_to.get("value") or raw.get("toValue") or raw.get("value")

    normalized = {
        "tx_hash": raw.get("transactionHash") or raw.get("txid") or raw.get("hash") or raw.get("id"),
        "chain": raw.get("chain"),
        "timestamp": raw.get("blockTimestamp") or raw.get("timestamp") or raw.get("time"),

        "from_address": from_obj.get("address"),
        "from_name": from_entity.get("name") or from_label.get("name"),
        "from_entity_id": from_entity.get("id"),
        "from_entity_type": from_entity.get("type"),
        "from_label_name": from_label.get("name"),

        "to_address": to_obj.get("address"),
        "to_name": to_entity.get("name") or to_label.get("name"),
        "to_entity_id": to_entity.get("id"),
        "to_entity_type": to_entity.get("type"),
        "to_label_name": to_label.get("name"),

        "token_symbol": raw.get("tokenSymbol"),
        "token_name": raw.get("tokenName"),
        "token_id": raw.get("tokenId"),

        "amount": amount,
        "usd_value": raw.get("historicalUSD") or raw.get("usdValue") or raw.get("usd"),

        "raw": raw,
    }
    return normalized


def is_exchange_label(name: Optional[str], entity_id: Optional[str], entity_type: Optional[str] = None) -> bool:
    text = " ".join([
        str(name or ""),
        str(entity_id or ""),
        str(entity_type or ""),
    ]).lower()

    exchange_keywords = [
        "binance",
        "coinbase",
        "kraken",
        "okx",
        "bybit",
        "kucoin",
        "upbit",
        "bitfinex",
        "gate",
        "exchange",
        "cex",
    ]
    return any(keyword in text for keyword in exchange_keywords)

def build_dex_stablecoin_alert(tx: Dict[str, Any], min_usd_value: float) -> Optional[Dict[str, Any]]:
    usd_value = tx.get("usd_value")
    if usd_value is None:
        return None

    try:
        usd_value = float(usd_value)
    except (TypeError, ValueError):
        return None

    token = (tx.get("token_symbol") or "").upper()
    if token not in {"USDC", "USDT"}:
        return None

    if usd_value < min_usd_value:
        return None

    if tx.get("from_entity_type") != "dex":
        return None

    tx_hash = tx.get("tx_hash") or "unknown_hash"
    protocol = tx.get("from_name") or "Unknown DEX"
    chain = tx.get("chain")

    return {
        "id": f"dex_flow:{tx_hash}:{token}",
        "type": "dex_stablecoin_flow",
        "message": (
            f"🔥 **DEX Stablecoin Flow**\n"
            f"Protocol: `{protocol}`\n"
            f"Token: `{token}`\n"
            f"USD: `${usd_value:,.2f}`\n"
            f"Chain: `{chain}`\n"
            f"Tx: `{tx_hash}`"
        ),
    }


def build_exchange_outflow_alert(tx: Dict[str, Any], min_usd_value: float) -> Optional[Dict[str, Any]]:
    usd_value = tx.get("usd_value")
    if usd_value is None:
        return None

    try:
        usd_value = float(usd_value)
    except (TypeError, ValueError):
        return None

    from_is_exchange = is_exchange_label(
        tx.get("from_name"),
        tx.get("from_entity_id"),
        tx.get("from_entity_type"),
    )
    to_is_exchange = is_exchange_label(
        tx.get("to_name"),
        tx.get("to_entity_id"),
        tx.get("to_entity_type"),
    )
    if tx.get("to_entity_id"):
        return None

    if not from_is_exchange:
        return None

    if to_is_exchange:
        return None

    if usd_value < min_usd_value:
        return None

    tx_hash = tx.get("tx_hash") or "unknown_hash"
    token_symbol = tx.get("token_symbol") or tx.get("chain") or "UNKNOWN"
    from_label = tx.get("from_name") or tx.get("from_label_name") or tx.get("from_entity_id") or "Unknown Exchange"
    to_label = tx.get("to_name") or tx.get("to_label_name") or tx.get("to_address") or "Unknown Wallet"
    chain = tx.get("chain") or "unknown-chain"

    return {
        "id": f"exchange_outflow:{tx_hash}:{token_symbol}",
        "type": "exchange_outflow",
        "message": (
            f"🚨 **Exchange Outflow**\n"
            f"From: `{from_label}`\n"
            f"To: `{to_label}`\n"
            f"Asset: `{token_symbol}`\n"
            f"USD: `${usd_value:,.2f}`\n"
            f"Chain: `{chain}`\n"
            f"Tx: `{tx_hash}`"
        ),
    }
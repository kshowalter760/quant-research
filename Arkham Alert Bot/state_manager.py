from collections import defaultdict
import time
from typing import Any, DefaultDict, Dict, List, Set, Tuple

from utils import load_json, save_json


class StateManager:
    def __init__(self, path: str) -> None:
        self.path = path
        self._seen = set(load_json(path, default=[]))

    def has_seen(self, alert_id: str) -> bool:
        return alert_id in self._seen

    def mark_seen(self, alert_id: str) -> None:
        self._seen.add(alert_id)
        save_json(self.path, sorted(self._seen))

    def all_seen(self) -> Set[str]:
        return set(self._seen)


class FlowTracker:
    def __init__(self, window_seconds: int = 900) -> None:
        self.window_seconds = window_seconds
        self.flows: DefaultDict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)

    def add(self, tx: Dict[str, Any]) -> Tuple[Tuple[str, str], List[Dict[str, Any]]]:
        protocol = tx.get("from_name") or "unknown_protocol"
        token = tx.get("token_symbol") or "UNKNOWN"
        entity_type = tx.get("from_entity_type")

        # Only track patterns from entity types we care about
        allowed_entity_types = {"dex", "cex"}
        if entity_type not in allowed_entity_types:
            return (protocol, token), []

        now = time.time()

        key = (protocol, token)

        self.flows[key].append(
            {
                "time": now,
                "usd": tx.get("usd_value"),
                "tx_hash": tx.get("tx_hash"),
            }
        )

        self.flows[key] = [
            flow
            for flow in self.flows[key]
            if now - flow["time"] < self.window_seconds
        ]

        return key, self.flows[key]


# 🔥 IMPORTANT: this must be OUTSIDE the class
def detect_repeated_flow(
    flows: List[Dict[str, Any]],
    min_count: int = 3,
    tolerance: float = 0.2,
    min_usd: float = 250_000,
) -> bool:
    """
    Detect repeated similar-sized meaningful flows within a time window.
    """

    filtered_flows = [
        flow
        for flow in flows
        if flow.get("usd") is not None and float(flow["usd"]) >= min_usd
    ]

    if len(filtered_flows) < min_count:
        return False

    values = [float(flow["usd"]) for flow in filtered_flows]

    avg = sum(values) / len(values)
    if avg == 0:
        return False

    similar = [
        value
        for value in values
        if abs(value - avg) / avg < tolerance
    ]

    return len(similar) >= min_count
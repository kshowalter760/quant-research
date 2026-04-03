import json
import os
from typing import Any, Dict, Iterable, Optional


def ensure_parent_dir(path: str) -> None:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)


def save_json(path: str, data: Any) -> None:
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(path: str, default: Any) -> Any:
    if not os.path.exists(path):
        return default

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def deep_get(obj: Any, paths: Iterable[str], default: Any = None) -> Any:
    """
    Try multiple dotted paths and return the first non-None value.
    Example path: "from.address" or "token.symbol"
    """
    for path in paths:
        current = obj
        ok = True

        for key in path.split("."):
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                ok = False
                break

        if ok and current is not None:
            return current

    return default


def first_item(data: Any) -> Optional[Dict[str, Any]]:
    if isinstance(data, list) and data:
        return data[0]
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, list) and value:
                return value[0]
    return None
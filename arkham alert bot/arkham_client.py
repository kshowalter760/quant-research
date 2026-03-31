import requests
from typing import Any, Dict, Optional

from config import settings


class ArkhamClient:
    def __init__(self, api_key: str, base_url: str) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        # Verify this header format against your Arkham account setup if needed.
        # The Arkham docs explicitly show API-Key header usage for WebSocket auth.
        self.session.headers.update({
            "API-Key": self.api_key,
            "Accept": "application/json",
        })

    def get_transfers(self, params: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.base_url}/transfers"
        response = self.session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def get_recent_transfers(
        self,
        time_last: str = "1h",
        limit: int = 25,
        usd_gte: Optional[float] = None,
        sort_key: str = "time",
        sort_dir: str = "desc",
        extra_params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        params: Dict[str, Any] = {
            "timeLast": time_last,
            "limit": limit,
            "sortKey": sort_key,
            "sortDir": sort_dir,
        }

        if usd_gte is not None:
            params["usdGte"] = usd_gte

        if extra_params:
            params.update(extra_params)

        return self.get_transfers(params=params)

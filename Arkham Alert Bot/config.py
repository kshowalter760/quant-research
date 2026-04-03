import os
from dataclasses import dataclass


@dataclass
class Settings:
    ARKHAM_API_KEY: str = os.getenv("ARKHAM_API_KEY", "c1103d21-7e5a-4b6a-a05a-d95bcba90530")
    ARKHAM_BASE_URL: str = os.getenv("ARKHAM_BASE_URL", "https://api.arkm.com")
    DISCORD_WEBHOOK_URL: str = os.getenv("DISCORD_WEBHOOK_URL", "https://discord.com/api/webhooks/1488653658001248297/IYwuvR99GRZuWBulEbcBCkEx-jX09ONMvPYjeaBsL4yaHhEyOEr-q16y5gOAHrzNVE0D")

    POLL_LIMIT: int = int(os.getenv("POLL_LIMIT", "25"))
    POLL_TIME_LAST: str = os.getenv("POLL_TIME_LAST", "1h")
    MIN_USD_VALUE: float = float(os.getenv("MIN_USD_VALUE", "500000"))

    RAW_OUTPUT_PATH: str = os.getenv("RAW_OUTPUT_PATH", "data/latest_transfers_raw.json")
    SEEN_ALERTS_PATH: str = os.getenv("SEEN_ALERTS_PATH", "data/seen_alerts.json")
    MIN_GLOBAL_USD = 10_000
    MIN_USD_VALUE = 10_000

settings = Settings()
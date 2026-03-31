import requests


class DiscordNotifier:
    def __init__(self, webhook_url: str) -> None:
        self.webhook_url = webhook_url

    def send_message(self, content: str) -> None:
        if not self.webhook_url:
            print("Discord webhook not configured. Skipping send.")
            return

        response = requests.post(
            self.webhook_url,
            json={"content": content},
            timeout=15,
        )
        response.raise_for_status()

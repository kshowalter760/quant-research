import random


random.seed(42)

EXCHANGES = ["Binance", "Coinbase", "Kraken"]
TOKENS = ["USDC", "USDT", "ETH", "SOL", "BTC"]
CHAINS = ["ethereum", "solana"]

BASE_TIMESTAMP = 1774923750


def random_usd():
    return random.choice([
        random.uniform(100_000, 400_000),
        random.uniform(500_000, 5_000_000),
    ])


def generate_mock_transfer(i):
    from_exchange = random.choice([True, False])

    return {
        "txHash": f"mock-tx-{i}",
        "chain": random.choice(CHAINS),
        "time": BASE_TIMESTAMP + i,
        "from": {
            "address": f"mock-from-{i}",
            "name": random.choice(EXCHANGES) if from_exchange else None,
        },
        "to": {
            "address": f"mock-to-{i}",
            "name": None if from_exchange else random.choice(EXCHANGES),
        },
        "token": {
            "symbol": random.choice(TOKENS),
            "name": "Mock Token",
        },
        "value": random.uniform(10, 1000),
        "usd": random_usd(),
    }


def generate_batch(n=20):
    return [generate_mock_transfer(i) for i in range(n)]
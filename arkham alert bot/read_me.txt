# Arkham On-Chain Alert Bot

A real-time Python-based signal engine that monitors on-chain activity using the Arkham API and detects meaningful capital flows across centralized exchanges (CEXs) and decentralized protocols (DEXs).

This project focuses on transforming raw blockchain data into actionable insights by filtering noise, identifying behavioral patterns, and delivering alerts via Discord.

---

## Overview

This bot continuously ingests live blockchain transfer data and applies a layered signal detection system:

* Filters out low-value noise
* Classifies entities (CEX, DEX, unlabeled wallets)
* Detects high-signal events (e.g., exchange outflows, DEX stablecoin flows)
* Identifies repeated structured flows (pattern detection)
* Sends real-time alerts to Discord

---

## Core Features

### 1. Data Ingestion

* Connects to Arkham API
* Fetches recent transfer activity
* Saves raw responses for inspection/debugging

### 2. Normalization Layer

* Converts inconsistent API payloads into a unified schema
* Handles multiple chain formats and nested structures

### 3. Signal Detection

#### Exchange Outflow Alert

Detects capital moving from centralized exchanges to external wallets.

#### DEX Stablecoin Flow Alert

Identifies stablecoin movement through decentralized protocols (potential deployment activity).

#### Repeated Flow Detection

Tracks and detects patterns of similar-sized transfers over short time windows.

---

## Architecture

```
arkham_alert_bot/
│
├── main.py                # Entry point (polling-based execution)
├── arkham_client.py      # API interaction layer
├── alerts.py             # Signal detection logic
├── state_manager.py      # Deduplication + pattern tracking
├── discord_notifier.py   # Discord webhook integration
├── utils.py              # Helper functions
├── config.py             # Environment + thresholds
└── data/
    └── seen_alerts.json  # Persistent state storage
```

---

## Signal Pipeline

```
Raw Transfers → Normalization → Global Filter → 
Event Alerts → Pattern Detection → Discord Notification
```

---

## Configuration

Set environment variables:

```bash
ARKHAM_API_KEY=your_api_key
DISCORD_WEBHOOK_URL=your_webhook_url
```

Adjust thresholds in `config.py`:

```python
MIN_GLOBAL_USD = 50_000      # Global filter threshold
MIN_USD_VALUE = 50_000       # Event alert threshold
```

---

## Running the Bot

```bash
python main.py
```

The bot will:

1. Fetch recent transfers
2. Normalize data
3. Apply filters and signal logic
4. Send alerts to Discord

---

## Example Alert

```
DEX Stablecoin Flow
Protocol: Aerodrome Finance
Token: USDC
USD: $1,200,000
Chain: Base
Tx: 0x...
```

---

## Design Philosophy

This project focuses on:

* Signal over noise — aggressive filtering to isolate meaningful activity
* Behavior over transactions — detecting patterns, not just events
* Modularity — clean separation between ingestion, logic, and alerts
* Extensibility — easy to add new alert types and strategies

---

## Future Improvements

* WebSocket-based real-time streaming (replace polling)
* Deployment to cloud infrastructure (e.g., DigitalOcean)
* Alert scoring and prioritization
* Wallet clustering and tracking
* Historical logging and analytics
* Multi-channel alert routing (Slack, email, etc.)

---

## Notes

* This project is designed for research and signal discovery, not execution
* Results depend heavily on market conditions and data availability
* Filtering thresholds may need adjustment over time

---

## Why This Matters

This tool demonstrates how raw blockchain data can be transformed into a structured signal system, similar to internal tooling used by quantitative trading desks and research teams.

---

## Tech Stack

* Python
* Requests
* Arkham API
* Discord Webhooks

---

## License

MIT License

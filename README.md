# Hype

Minimal skeleton for the Telegram escrow marketplace bot.

## Setup

1. Create virtual environment and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt -r requirements-dev.txt
   ```
2. Copy `.env.example` to `.env` and set your variables.
3. Run linters and tests:
   ```bash
   flake8
   pytest
   ```

Docker usage:
```bash
docker compose run --rm app
```


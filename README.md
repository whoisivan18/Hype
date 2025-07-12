# Hype Telegram Bot

This repository contains a simple Telegram bot that allows scheduling delayed messages.

## Setup

1. Copy `.env.example` to `.env` and set your Telegram bot token.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

Send `/schedule <minutes> <message>` in any chat with the bot. It will send `<message>` back to the chat after the specified number of minutes.

"""Simple Telegram bot with delayed posting feature."""

import os
from datetime import timedelta
from typing import List, Tuple

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()


def parse_schedule_args(args: List[str]) -> Tuple[int, str]:
    """Return minutes and message parsed from command arguments."""
    if len(args) < 2:
        raise ValueError("Missing arguments")
    minutes = int(args[0])
    message = " ".join(args[1:])
    return minutes, message


TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message."""
    await update.message.reply_text(
        "Send /schedule <minutes> <message> to schedule a message."
    )


async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Schedule a message after given minutes."""
    try:
        minutes, message = parse_schedule_args(context.args)
    except ValueError:
        await update.message.reply_text("Usage: /schedule <minutes> <message>")
        return

    delay = timedelta(minutes=minutes)

    def send_message(context: ContextTypes.DEFAULT_TYPE) -> None:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message
        )

    context.job_queue.run_once(send_message, delay)
    await update.message.reply_text(f"Message scheduled in {minutes} minutes")


def main() -> None:
    if TOKEN is None:
        raise RuntimeError("TELEGRAM_TOKEN is not set in environment")
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("schedule", schedule))

    application.run_polling()


if __name__ == "__main__":
    main()

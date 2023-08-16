from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from typing import final
from App import getBestAnswer

BOT_TOKEN: final = "6430121596:AAELsUQzkMJ3cDMziPPiyWqWYOtsqEernLQ"

USERNAME: final = "DNC-AI"


async def handle_response(message: str) -> str:
    return getBestAnswer(message)


async def handle_Message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    userID: str = update.message.chat.full_name
    text: str = update.message.text.lower()
    print(f"{userID} sent {text}")
    response: str = await handle_response(text)
    print(f"{USERNAME} responded {response}")
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused {context.error}")


if __name__ == "__main__":
    print("Starting bot")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_Message))
    app.add_error_handler(error)

    app.run_polling()

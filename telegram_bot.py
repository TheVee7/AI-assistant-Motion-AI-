from typing import final
from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler , filters
from telegram.ext import ContextTypes , CallbackContext

TOKEN: final = "6935894815:AAFvNkrhv2MKVVQmxQzS2yrnPinbi2F1AIw"
BOT_USERNAME: final = "@vee_ka_bot"

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text("hello , guys how are you")

def handle_response(text: str):
    a: str = text.lower()
    print(f"Lowercased text: {a}")
    if "varun" in a:
        return "Hello, Auth pass. What do you want to do?"
    else:
        return "Auth failed"

    
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start_command))

    print("starting")
    app.run_polling(poll_interval=3)
    response = handle_response("This is a message with varun")
    print(response)

    
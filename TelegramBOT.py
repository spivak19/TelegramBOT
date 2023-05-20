# import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

url = "https://dj2eon0iy1.execute-api.eu-north-1.amazonaws.com/TelegramBot"
api ="6057836089:AAFa9pr5GGxbO8jacDwi6sBNa2-2FMMO_Ek"
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )


async def send_picture(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the chat ID of the user
    chat_id = update.message.chat_id

    # Send the picture
    await context.bot.send_photo(chat_id=chat_id, photo=open('Image.jpg', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="זה הרמז שלכם")

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="ברוכים הבאים ענף ניווט וזמן")


if __name__ == '__main__':
    application = ApplicationBuilder().token(api).build()

    # start_handler = CommandHandler('start', start)
    start_handler = CommandHandler('start', send_picture)
    application.add_handler(start_handler)

    application.run_polling()
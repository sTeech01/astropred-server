from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Функция отправки приветственного сообщения с кнопкой
async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть приложение", url="https://t.me/astropred_bot?start=app")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔮 Привет! Я — астробот.\nНажми на кнопку ниже, чтобы открыть приложение!",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    # Твой токен
    TOKEN = "7494465986:AAHEcDJbQ_MORjLojI3Q5jMerHh60D8k1Qc"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Обработка команды /start
    app.add_handler(CommandHandler("start", send_welcome))
    
    # Обработка любых текстовых сообщений, чтобы тоже показывать приветствие
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), send_welcome))
    
    app.run_polling()

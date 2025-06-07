from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 Привет! Я — астробот. Готов показать, что звёзды приготовили именно тебе!
Жми на кнопку внизу, чтобы открыть приложение 👇"
    )

app = ApplicationBuilder().token("7494465986:AAHEcDJbQ_MORjLojI3Q5jMerHh60D8k1Qc").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

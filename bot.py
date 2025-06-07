from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 Привет! Я — астробот. Жми на кнопку внизу, чтобы открыть астроприложение 👇"
    )

app = ApplicationBuilder().token("7494465986:AAHEcDJbQ_MORjLojI3Q5jMerHh60D8k1Qc").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

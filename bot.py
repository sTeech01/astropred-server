from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 Привет! Я — астробот. Жми на кнопку внизу, чтобы открыть астроприложение 👇"
    )

app = ApplicationBuilder().token("ТВОЙ_ТОКЕН_ОТ_BOTFATHER").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

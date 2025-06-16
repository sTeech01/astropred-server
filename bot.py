from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Функция для приветственного сообщения
async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Открыть астроприложение", callback_data='open_app')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message = (
        "<b>ПОЛУЧИ ЛИЧНЫЙ АСТРОПРОФИЛЬ</b>\n"
        "<i>Всего 5 минут — и звёзды заговорят</i>\n\n"
        "🔮 Привет! Я — Астродамус, твой личный астропомощник. Жми на кнопку внизу, чтобы открыть астроприложение 👇"
    )

    await update.message.reply_html(message, reply_markup=reply_markup)

async def button(update, context):
    query = update.callback_query
    await query.answer()
    if query.data == 'open_app':
        await query.edit_message_text("Вы открыли астроприложение! Скоро начнём анализ твоих звёзд. 🌟")

def main():
    application = Application.builder().token("7494465986:AAHEcDJbQ_MORjLojI3Q5jMerHh60D8k1Qc").drop_pending_updates(True).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()

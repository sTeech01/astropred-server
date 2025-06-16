from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Функция для приветственного сообщения
async def start(update, context):
    # Создаем инлайн-клавиатуру с кнопкой
    keyboard = [
        [InlineKeyboardButton("Получить 100 бонусов", callback_data='get_bonus')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Форматированное сообщение с HTML
    message = (
        "<b>ПОЛУЧИ ДО 100 БОНУСОВ</b>\n"
        "<i>Через 5 минут онлайн</i>\n\n"
        "Что может делать этот бот?\n"
        "🔮 Привет! Я — астробот. Жми на кнопку внизу, чтобы открыть астроприложение 👇"
    )

    await update.message.reply_html(message, reply_markup=reply_markup)

async def button(update, context):
    query = update.callback_query
    await query.answer()
    if query.data == 'get_bonus':
        await query.edit_message_text("Вы нажали на кнопку! Бонусы скоро будут начислены.")

# Настройка бота
def main():
    # Замените "ВАШ_ТОКЕН_БОТА" на ваш токен
    application = Application.builder().token("7494465986:AAHEcDJbQ_MORjLojI3Q5jMerHh60D8k1Qc").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()

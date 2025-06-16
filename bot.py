from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция для приветственного сообщения
def start(update, context):
    # Создаем инлайн-клавиатуру с кнопкой
    keyboard = [
        [InlineKeyboardButton("Получить доступ к крытому инструменту", callback_data='get_bonus')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Форматированное сообщение с HTML
    message = (
        "<b>Узнай свое будущее</b>\n"
        "<i>Простой и красивый интерфейс. Узнай</i>\n\n"
        "Что может делать этот бот?\n"
        "🔮 Привет! Я — астробот. Жми на кнопку внизу, чтобы открыть астроприложение 👇"
    )

    update.message.reply_html(message, reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'get_bonus':
        query.edit_message_text("Вы нажали на кнопку! Бонусы скоро будут начислены.")

# Настройка бота
def main():
    updater = Updater("7494465986:AAHEcDJbQ_MORjLojI3Q5jMerHh60D8k1Qc", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackContext.callback_query_handler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

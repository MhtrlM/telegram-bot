import logging

from telegram import User, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start_callback(update, context):
    user: User = update.message.from_user
    greeting_message = f"Привет новый пользователь {user.first_name} {user.username}"

    buttons = []

    button1 = [InlineKeyboardButton(text='Начать покупки', callback_data='start_shopping')]
    button2 = [InlineKeyboardButton(text='Отследить заказ', callback_data='check_order')]

    buttons.append(button1)
    buttons.append(button2)

    logger.error(f"User sent incorrect data {user.username}")

    print("Тут кнопки отправились")

    # update.message.reply_text(
    #     greeting_message,
    #     reply_markup=InlineKeyboardMarkup(buttons, one_time_keyboard=True))


def main():
    """Run bot."""
    updater = Updater(token="-----", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # simple start function
    dp.add_handler(CommandHandler("start", start_callback))

    # Add command handler to start the payment invoice
    # dp.add_handler(CommandHandler("shipping", start_with_shipping_callback))
    # dp.add_handler(CommandHandler("noshipping", start_without_shipping_callback))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    logger.info("My bot is starting  NOW")
    main()

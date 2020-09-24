# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from uuid import uuid4
from telegram.ext import Updater, CommandHandler


Token = "1348108725:AAGXYpvTbjn6AfpN0UYzgojVEAEGBoZfjiE"


def put(update, context):
    key = uuid4()
    value = update.message.text.partition(' ')[2]

    context.user_data[key] = value

    update.message.reply_text(key)


def get(update, context):
    key = update.message.text.partition(' ')[2]

    try:
        value = context.user_data[key]
        update.message.reply_text(update.message.from_user)

    except KeyError:
        update.message.reply_text("Not found")


if __name__ == '__main__':
    updater = Updater(token=Token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('put', put))
    dp.add_handler(CommandHandler('get', get))

    updater.start_polling()
    updater.idle()
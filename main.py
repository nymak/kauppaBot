from telegram.ext import Updater, CommandHandler, Filters
import logging
from commands.get import get, getMonth, getLastMonth
from commands.put import put
from commands.secrets import ChatID, Token

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    updater = Updater(token=Token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('put', put, filters=Filters.chat((ChatID,))))
    dp.add_handler(CommandHandler('get', get, filters=Filters.chat((ChatID,))))
    dp.add_handler(CommandHandler('getmonth', getMonth, filters=Filters.chat((ChatID,))))
    dp.add_handler(CommandHandler('getlast', getLastMonth, filters=Filters.chat((ChatID,))))

    updater.start_polling()
    updater.idle()

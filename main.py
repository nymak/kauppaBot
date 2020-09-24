import json
from telegram.ext import Updater, CommandHandler, Filters
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


Token = "1348108725:AAGXYpvTbjn6AfpN0UYzgojVEAEGBoZfjiE"
ID = {"Emma": "1083152001", "Markus": "969398103/"}
ChatID = -280850961

def onMessage(update):
    if update.message.chat_id != ChatID:
        return

def splitDate(date):
    date = date.split("-")
    return date[1]

def readJson(filename="data.json"):
    with open(filename, "r") as f:
        return json.load(f)

def writeJson(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def checkSender(key):
    if key not in ID.values():
        return

def checkMonthAndAdd(data, key, month):
    total = 0
    for date in data[key].keys():
        if splitDate(date) == month:
            total += data[key][date]
    return total


def put(update, context):
    onMessage(update)
    key1 = str(update.message.from_user["id"])
    checkSender(key1)
    key2 = str(update.message.date.date())
    try:
        value = int(update.message.text.partition(' ')[2])
    except ValueError:
        update.message.reply_text("Invalid input")
        return None
    data = readJson()
    data[key1][key2] = value
    writeJson(data)
    update.message.reply_text("Success")


def getTotal(update, context):
    onMessage(update)
    data = readJson()
    total = 0
    for key in data.keys():
        total += sum(data[key].values())

    update.message.reply_text(f"{total}€")


def getMonth(update, context):
    onMessage(update)
    key = str(update.message.from_user["id"])
    month = splitDate(str(update.message.date.date()))
    checkSender(key)
    data = readJson()
    total = checkMonthAndAdd(data, key, month)
    update.message.reply_text(f"{total}€")


def getMonthTot(update, context):
    onMessage(update)
    month = splitDate(str(update.message.date.date()))
    data = readJson()
    total = 0
    for key in data.keys():
        total += checkMonthAndAdd(data, key, month)
    update.message.reply_text(f"{total}€")

def get(update, context):
    onMessage(update)
    key = str(update.message.from_user["id"])
    checkSender(key)
    data = readJson()
    try:
        value = sum(data[key].values())
        update.message.reply_text(value)

    except KeyError:
        update.message.reply_text("Not found")


if __name__ == '__main__':
    updater = Updater(token=Token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('put', put, filters=Filters.chat((ChatID,))))
    dp.add_handler(CommandHandler('get', get, filters=Filters.chat((ChatID,))))
    dp.add_handler(CommandHandler('gettot', getTotal, filters=Filters.chat((ChatID,))))
    dp.add_handler(CommandHandler('getmonth', getMonth, filters=Filters.chat((ChatID,))))
    dp.add_handler(CommandHandler('getmonthtot', getMonthTot, filters=Filters.chat((ChatID,))))

    updater.start_polling()
    updater.idle()

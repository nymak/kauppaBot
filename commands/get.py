import commands.helper as helper
from functools import reduce


def get(update, context):
    helper.onMessage(update)
    helper.checkSender(str(update.message.from_user["id"]))
    data = helper.readJson()
    key1 = list(data.keys())[0]
    key2 = list(data.keys())[1]
    total1 = reduce(lambda a, b: a+b, data[key1].values())
    total2 = reduce(lambda a, b: a+b, data[key2].values())
    update.message.reply_text(f"Emma: {round(total1, 2)}€\nMarkus: {round(total2, 2)}€\nTotal: {round(total1+total2, 2)}€")


def getMonth(update, context):
    helper.onMessage(update)
    helper.checkSender(str(update.message.from_user["id"]))
    month = helper.splitDate(str(update.message.date.date()))
    data = helper.readJson()
    key1 = list(data.keys())[0]
    key2 = list(data.keys())[1]
    total1 = helper.checkMonthAndAdd(data, key1, month)
    total2 = helper.checkMonthAndAdd(data, key2, month)
    update.message.reply_text(f"Emma: {round(total1, 2)}€\nMarkus: {round(total2, 2)}€\nTotal: {round(total1+total2, 2)}€")


def getLastMonth(update, context):
    helper.onMessage(update)
    helper.checkSender(str(update.message.from_user["id"]))
    month = str(int(helper.splitDate(str(update.message.date.date()))) - 1).zfill(2)
    print(month)
    data = helper.readJson()
    key1 = list(data.keys())[0]
    key2 = list(data.keys())[1]
    total1 = helper.checkMonthAndAdd(data, key1, month)
    total2 = helper.checkMonthAndAdd(data, key2, month)
    update.message.reply_text(f"Emma: {round(total1, 2)}€\nMarkus: {round(total2, 2)}€\nTotal: {round(total1+total2, 2)}€")
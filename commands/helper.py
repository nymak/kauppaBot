import json
import commands.secrets as secrets


def onMessage(update):
    if update.message.chat_id != secrets.ChatID:
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
    if key not in secrets.ID.values():
        return


def checkMonthAndAdd(data, key, month):
    total = 0
    for date in data[key].keys():
        if splitDate(date) == month:
            total += data[key][date]
    return total
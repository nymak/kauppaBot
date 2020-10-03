import commands.helper as helper


def put(update, context):
    helper.onMessage(update)
    key1 = str(update.message.from_user["id"])
    helper.checkSender(key1)
    key2 = str(update.message.date.date())
    try:
        value = int(update.message.text.partition(' ')[2])
    except ValueError:
        update.message.reply_text("Invalid input")
        return None
    data = helper.readJson()
    data[key1][key2] = value
    helper.writeJson(data)
    update.message.reply_text("Success")
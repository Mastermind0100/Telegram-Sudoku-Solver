from telegram.ext import Updater, MessageHandler, Filters
import telegram
import logging
from telegram.ext import CommandHandler
import requests
import re
final = []

def echo(incoming, outgoing):
    chat_id = incoming.effective_chat.id
    outgoing.bot.send_message(chat_id=chat_id, text="Here is the Solved Sudoku")
    f = open("solved.txt")
    for i in range (0,9):
        text = f.readline()
        final.append(text)
    f.close()
    print(final)
    for i in final:
        outgoing.bot.send_message(chat_id=chat_id, text=i)
    os.remove("solved.txt")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='<Enter Token Here>', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
updater.idle()


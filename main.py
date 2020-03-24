import logging
import urllib.request
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import os
import bot
 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(incoming, outgoing):
    outgoing.bot.send_message(chat_id=incoming.effective_chat.id, text="I think I got the Solution...")

def image(incoming, outgoing):
    photo = incoming.get_file(outgoing.effective_message.photo[-1].file_id)
    filename = 'test.png'
    urllib.request.urlretrieve(photo["file_path"],filename)
    os.system("main.py 1")
    os.system("bot.py 1")
    
updater = Updater('<Ennter Token Here>')
dp = updater.dispatcher
dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.photo, image))
updater.start_polling()
updater.idle()
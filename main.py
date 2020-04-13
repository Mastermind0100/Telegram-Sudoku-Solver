import logging
import urllib.request
import os

from telegram.ext import Updater, MessageHandler, Filters
 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def solver(bot, update):
    pass
    if not update.effective_message.photo:
        update.effective_message.reply_text(text = "Please send me an image... Preferrably of a Sudoku... Thanks...")
    else:
        photo = bot.get_file(update.effective_message.photo[-1].file_id)
        urllib.request.urlretrieve(photo["file_path"],'test.png')
        update.effective_message.reply_text(text = "Image Recieved!")
        update.effective_message.reply_text(text = "Solving the Sudoku Now")
        os.system("main.py 1")
        update.effective_message.reply_text(text = "-----------Solved-----------")
        file = open('solved.txt')
        for i in range(0,10):
            text = file.readline()
            update.effective_message.reply_text(text = text)
        file.close()
        update.effective_message.reply_text(text = "Did I solve it right?")
       
def main():
    updater = Updater('<Enter bot token here>')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, solver))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
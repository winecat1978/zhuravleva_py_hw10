from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler

bot = Bot(token='5485842776:AAFrwnwjTiTtHIUbztQBQFx6000ajP815aw')
updater = Updater(token='5485842776:AAFrwnwjTiTtHIUbztQBQFx6000ajP815aw')
dispatcher = updater.dispatcher

START = 0
NUMBERFIRST = 1
NUMBERSECOND = 2
OPERATION = 3

def numbers(number):
    pass

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать!')

    return START

updater.start_polling()
updater.idle()
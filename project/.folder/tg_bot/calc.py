from telegram import Bot
#from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, Filters, ContextTypes, ConversationHandler
from commands import *

#app = ApplicationBuilder().token('5552127770:AAHt_ib8rm6AjOqcErAxZdjBqr57jJaegLU').build()
bot = Bot(token='5552127770:AAHt_ib8rm6AjOqcErAxZdjBqr57jJaegLU')
updater = Updater(token='5552127770:AAHt_ib8rm6AjOqcErAxZdjBqr57jJaegLU')
dispatcher = updater.dispatcher

bot.add_handler(CommandHandler("Hi", hi_command))
bot.add_handler(CommandHandler("Time", time_command))
bot.add_handler(CommandHandler("Help", help_command))
bot.add_handler(CommandHandler("sum", sum_command))
bot.add_handler(CommandHandler("min", minus_command))
bot.add_handler(CommandHandler("mult", pow_command))
bot.add_handler(CommandHandler("div", div_command))
bot.add_handler(CommandHandler("exp", exponent_command))
bot.add_handler(CommandHandler("c_sum", complex_sum_command))
bot.add_handler(CommandHandler("c_min", complex_min_command))
bot.add_handler(CommandHandler("c_mult", complex_mult_command))
bot.add_handler(CommandHandler("c_div", complex_div_command))
bot.add_handler(CommandHandler("CandyGame", start_game))
turn_handler = MessageHandler(Filters.text,WhoPlaysFirst)
play_handler = MessageHandler(Filters.text, Play)
cancel_handler = MessageHandler(Filters.text, cancel_command)
conv_handler = ConversationHandler(fallbacks=["CandyGame"],
                                    states={
                                        START:[turn_handler],
                                        TURN: [play_handler],
                                    },
                                    entry_points=[cancel_handler])

print("server start")
updater.start_polling()
updater.idle
bot.run_polling()
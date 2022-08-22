from telegram import Update
from telegram.ext import Filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, ConversationHandler
import datetime
import random

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Базовые команды:\n/Hi(Привет!)\n/Time(Который час?)\n/Help(Помоги!)\n\nДействия с рациональными числами:\nПример ввода: 12 23\nСумма(/sum)\nРазность(/min)\nУмножение(/mult)\nДеление(/div)\nВозведение в степень(/exp)\n\n\
Действия с комплексными числами:\nПример ввода: 1 2 3 4 -> 1+2j и 3+4j\nСумма(/c_sum)\nРазность(/c_min)\nУмножение(/c_mult)\nДеление(/c_div)\n/CandyGame')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}+{y} = {x+y}')

async def minus_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    msg = update.message.text
    print(msg)
    items = msg.split() 
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}-{y} = {x-y}')

async def pow_command(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}*{y} = {x*y}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} : {y} = {x/y}')

async def exponent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}^{y} = {x**y}')

async def complex_sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 4324
    print(items)
    a = complex(float(items[1]),float(items[2]))
    b = complex(float(items[3]),float(items[4]))
    await update.message.reply_text(f'{a}+{b} = {a+b}')

async def complex_min_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 4324
    print(items)
    a = complex(float(items[1]),float(items[2]))
    b = complex(float(items[3]),float(items[4]))
    await update.message.reply_text(f'{a}-{b} = {a-b}')

async def complex_mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 4324
    print(items)
    a = complex(float(items[1]),float(items[2]))
    b = complex(float(items[3]),float(items[4]))
    await update.message.reply_text(f'{a}*{b} = {a*b}')

async def complex_div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 4324
    print(items)
    a = complex(float(items[1]),float(items[2]))
    b = complex(float(items[3]),float(items[4]))
    await update.message.reply_text(f'{a} : {b} = {a/b}')


START = 0
TURN = 1


def start_game(update, context):
    global smt
    context.bot.send_message(update.effective_chat.id,'Добро пожаловать в игру на логику и счет "Конфетки"! Напиши что-нибудь: ')
    smt = str(update.message.text)
    return START

def WhoPlaysFirst (update, context):
    global answer
    context.bot.send_message('{update.effective_user.first_name}, как зовут вашего противника?')
    pl_2_name = update.message.text
    context.bot.send_message('{update.effective_user.first_name}, ваш выбор: орел или решка?')
    player1 = update.message.text
    player2 = ''
    if player1 == 'орел':
       player2 = 'решка'
    elif player1 == 'решка':
        player2 = 'орел'
    context.bot.send_message(f'{pl_2_name}, вы выбрали вариант {player2}.')

    orel = [0,'орел']
    reshka = [1,'решка']
    a = random.randrange(0,2)
    context.bot.send_message('*Подкидываем воображаемую монетку*')
    if a == orel[0]:
        if orel[1] == player1:
            answer = f'Орел!{update.effective_user.first_name}, ваш ход!'
        if orel[1] == player2:
            answer = f'Орел!{pl_2_name}, ваш ход!'

    if a == reshka[0]:
        if reshka[1] == player1:
            answer = f'Решка{update.effective_user.first_name}, ваш ход!'
        if reshka[1] == player2:
            answer = f'Решка!{pl_2_name}, ваш ход!'
    return TURN

def Play(update, context):
    all_in_all = 2021
    player1 = 0
    player2 = 0
    context.bot.send_message(f'\nПриступим!\nНа столе лежит 2021 конфета.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n ')
    while all_in_all > 0:
        if first == True:
            context.bot.send_message("Игрок №1, делайте ход.")
            step1 = GetNumber(1)
            player1+=step1
            all_in_all -=step1
            context.bot.send_message(f'\nИтого: {all_in_all}\nПервый игрок:{player1}\nВторой игрок:{player2}')
            first = False
        else:
            context.bot.send_message("Игрок №2, делайте ход.")
            step2 = GetNumber(1)
            player2+=step2
            all_in_all-=step2
            context.bot.send_message(f'\nИтого: {all_in_all}\nПервый игрок:{player1}\nВторой игрок:{player2}')
            first = True
    
    if all_in_all == 0:
        if first == True:
            player2 += player1
            player1 = 0
            context.bot.send_message(f'\n Поздравляем! Победил Игрок №2\nПервый игрок:{player1}\nВторой игрок:{player2}')
        if first == False:
            player1+=player2
            player2 = 0
            context.bot.send_message(f'\nПоздравляем! Победил Игрок №1\nПервый игрок:{player1}\nВторой игрок:{player2}')

    def GetNumber(update, context, x): 
        num = 0
        for i in range (x):
            smt = False
            while not smt:
                try:
                    context.bot.send_message("Выберите число от 1 до 28: ")
                    number = int(update.message.text)
                    num = number
                    smt = True
                    if number < 1 or number > 28:
                        smt = False
                        context.bot.send_message("Выберите число от 1 до 28!")
                except ValueError:
                    context.bot.send_message("Вы ошиблись. Введите число!")
            return num

def cancel_command(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')
    return ConversationHandler.END

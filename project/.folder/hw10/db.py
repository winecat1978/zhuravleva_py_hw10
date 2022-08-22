# import telebot;
# from telebot import types
# bot = telebot.TeleBot('5485842776:AAFrwnwjTiTtHIUbztQBQFx6000ajP815aw');

# @bot.message_handler(content_types=['text'])
#  def get_text_messages(message):
#     if message.text == "/help":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?\n Если хочешь импортировать данные, напиши /import,\nЕсли хочешь экспортировать данные, введи /export")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши Привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# name = ''
# surname = ''
# age = 0
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/import':
#         bot.send_message(message.from_user.id, "Как тебя зовут?");
#         bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /import');

# def get_name(message): #получаем фамилию
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
#     bot.register_next_step_handler(message, get_surname);

# def get_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message(message.from_user.id,'Сколько тебе лет?')
#     bot.register_next_step_handler(message, get_age)

# def get_age(message):
#     global age;
#     while age == 0: #проверяем что возраст изменился
#         try:
#              age = int(message.text) #проверяем, что возраст введен корректно
#         except Exception:
#              bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
#         bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

# def get_age(message):
#     global age;
#     while age == 0: #проверяем что возраст изменился
#         try:
#              age = int(message.text) #проверяем, что возраст введен корректно
#         except Exception:
#              bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
#         keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
#         key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
#         keyboard.add(key_yes); #добавляем кнопку в клавиатуру
#         key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
#         keyboard.add(key_no);
#         question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
#         ... #код сохранения данных, или их обработки
#         bot.send_message(call.message.chat.id, 'Запомню : )');
#     elif call.data == "no":
#          ... #переспрашиваем

# bot.polling(none_stop=True, interval=0)
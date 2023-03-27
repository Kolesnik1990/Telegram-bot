import telebot
from config import token


mybot = telebot.TeleBot(token)
name = ''
@mybot.message_handler(commands=['start'])
def start_mess(message):
    mybot.send_message(message.chat.id, 'Привет, мой дорогой друг!')
    markup = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton('привет')
    btn2 = telebot.types.KeyboardButton('/help')
    btn3 = telebot.types.KeyboardButton('Еще одна кнопка')
    markup.row(btn1, btn2)
    markup.row(btn3)
    mybot.send_message(message.chat.id, 'Мы тут сделали управление:', reply_markup=markup)
    with open('texttext.txt', 'a') as f:
        print(message.text, file=f)
        print(message.from_user.username, file=f)


@mybot.message_handler(commands=['help'])
def help_mess(message):
    mybot.send_message(message.chat.id, 'Раздел помощи находится в разработке')
    print(message.from_user.id)

@mybot.message_handler(content_types=['text'])
def hello_mess(message):
    if message.text.lower() == 'привет':
        mybot.send_message(message.chat.id, 'И тебе привет!')
        mybot.send_message(message.chat.id, 'Как тебя зовут?')
        mybot.register_next_step_handler(message, reg_name)
def reg_name(message):
    global name
    name = message.text
    mybot.send_message(message.chat.id, f'Рад приветствовать тебя {name}')
    my_keyboard = telebot.types.InlineKeyboardMarkup()
    key_one = telebot.types.InlineKeyboardButton(text='Больше 18', callback_data='1')
    key_two = telebot.types.InlineKeyboardButton(text='Меньше 18', callback_data='2')
    my_keyboard.add(key_one)
    my_keyboard.add(key_two)
    mybot.send_message(message.chat.id, 'Сколько тебе лет?', reply_markup=my_keyboard)

@mybot.callback_query_handler(func=lambda call: True)
def callback_keyboard(call):
    if call.data == '1':
        mybot.send_message(call.message.chat.id, 'Тебе уже можно всё')
    if call.data == '2':
        mybot.send_message(call.message.chat.id, 'Пока ничего нельзя!')

mybot.infinity_polling()
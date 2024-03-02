import buttons
import telebot
from telebot import types

# Bot's object was created
bot = telebot.TeleBot("6923031258:AAF9Ar0Rz5mGrxdT003O-i8688v1BtJY3vc")


@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Welcome :)", reply_markup=buttons.language())


@bot.message_handler(commands=["my_git_hub"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "https://github.com/zok1rjonoff")


@bot.message_handler(content_types=["text"])
def text(message):
    user_id = message.from_user.id
    if message.text == "English":
        bot.send_message(user_id, f"Welcome {message.from_user.first_name}", reply_markup=buttons.menu_en())
    elif message.text == "Russian":
        bot.send_message(user_id, f"Добро пожаловать {message.from_user.first_name}",
                         reply_markup=buttons.menu_ru())
    elif message.text.lower() == "From ... to UZS".lower():
        bot.send_message(user_id, f"Welcome:)", reply_markup=buttons.ccy_button_en())
    elif message.text.lower() == "Dictionary".lower():
        bot.send_message(user_id, f"Available words:\n{buttons.words} \n"
                                  f"Write one them ")
    elif message.text.lower() == "Wikipedia".lower():
        bot.send_message(user_id, "Choose", reply_markup=buttons.wikipedia_en())
        bot.register_next_step_handler(message, wikipedia_en, user_id)

    elif message.text == "From UZS to ...":
        bot.send_message(user_id, "Welcome:)", reply_markup=buttons.ccy_button_en())
        bot.register_next_step_handler(message, from_uzs, user_id)

    elif message.text == "С ... НА UZS":
        bot.send_message(user_id, f"Добро пожаловать:)", reply_markup=buttons.ccy_button_ru())

    elif message.text == "Info about currency":
        bot.send_message(user_id, "Press the button to know information about certain currency",
                         reply_markup=buttons.inline_currency_en())

    elif message.text == "Словарь":
        bot.send_message(user_id, f"Доступные слова:\n{buttons.words_1} \n"
                                  f"Напишите один из них")
    elif message.text == "Информация о валютах":
        bot.send_message(user_id, "Выберите один из них", reply_markup=buttons.inline_currency_ru())

    elif message.text == "Википедия":
        bot.send_message(user_id, "Выберите один из них", reply_markup=buttons.wikipedia_ru())
        bot.register_next_step_handler(message, wikipedia_ru, user_id)
    elif message.text == "С UZS НА ...":
        bot.send_message(user_id, "Welcome:)", reply_markup=buttons.ccy_button_ru())
        bot.register_next_step_handler(message, from_uzs, user_id)
    elif message.text in buttons.lis_ccy_ru:
        ccy = message.text[:3]
        bot.send_message(user_id, "Введите сумму", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, calculate_from_foreign, ccy, user_id)
    elif message.text in buttons.lis_ccy_en:
        ccy = message.text[:3]
        bot.send_message(user_id, "Enter the sum", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, calculate_from_foreign, ccy, user_id)
    elif message.text.lower() in buttons.dictionary_ru.keys():
        print(message.text)
        bot.send_message(user_id, buttons.dictionary_ru[message.text.lower()], reply_markup=buttons.language())
    else:
        bot.send_message(user_id, "Something went wrong")


@bot.callback_query_handler(lambda call: True)
def ccy_en(call):
    chat_id = call.message.chat.id
    if call.data in buttons.lis_ccy_en:
        whole = buttons.info_about_ccy_en(call.data)
        bot.send_message(chat_id, whole, reply_markup=buttons.menu_en())
    else:
        whole = buttons.info_about_ccy_ru(call.data)
        bot.send_message(chat_id, whole)


def calculate_from_foreign(message, ccy, user_id):
    money = float(message.text)
    total = buttons.rate(money, ccy, "UZS")
    bot.send_message(user_id, total, reply_markup=buttons.menu_ru())


def calculate_from_uzs(message, ccy, user_id):
    money = float(message.text)
    total = buttons.rate(money, ccy, "UZS")
    bot.send_message(user_id, total, reply_markup=buttons.menu_en())


def from_uzs(message, user_id):
    ccy = message.text
    if ccy in buttons.lis_ccy_en:
        bot.send_message(user_id, "Enter the sum in UZS", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, calculation_from_uzs, ccy[:3], user_id)
    else:
        bot.send_message(user_id, "Введите сумму в UZS", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, calculation_from_uzs, ccy, user_id)


def calculation_from_uzs(message, ccy, user_id):
    if ccy in buttons.lis_ccy_en:
        if message.text.isdecimal():
            money = float(message.text)
            total = buttons.from_uzs_to_foreign(money, "UZS", ccy[:3])
            bot.send_message(user_id, total, reply_markup=buttons.language())
        else:
            bot.send_message(user_id, "Please enter the sum correctly")
    else:
        if message.text.isdecimal():
            money = float(message.text)
            total = buttons.from_uzs_to_foreign(money, "UZS", ccy[:3])
            bot.send_message(user_id, total, reply_markup=buttons.language())
        else:
            bot.send_message(user_id, "Рожалуйста введите сумму правильно")


def wikipedia_ru(message, user_id):
    bot.send_message(user_id, buttons.wikipedia_dic_ru[message.text.lower()], reply_markup=buttons.language())


def wikipedia_en(message, user_id):
    bot.send_message(user_id, buttons.wikipedia_dic_en[message.text.lower()], reply_markup=buttons.language())


bot.polling(non_stop=True)

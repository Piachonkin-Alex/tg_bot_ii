import telebot
import sqlite3
import numpy as np
from telebot import types
import json

bot = telebot.TeleBot("5301718610:AAG3d_zTCJZzyiwQmN8EfJNtIO7tmdawg0A")
with open('database_films.db', 'a+') as _:
    pass
conn = sqlite3.connect('database_films.db', check_same_thread=False)

state = "before start"  # begin, 1, 2, 3 , -> end -> return res

channels = [{'name': 'Java для начинающих', 'chan': 'https://www.youtube.com/channel/UCvuY904el7JvBlPbdqbfguw',
             'playlist': 'https://www.youtube.com/watch?v=Zxpz5tRrUvU&list=PL0lO_mIqDDFW2xXiWSfjT7hEdOUZHVNbK&index=1',
             'links': ['https://youtu.be/Zxpz5tRrUvU', 'https://youtu.be/AM_WxaR6Spc', 'https://youtu.be/IQTEziR82so',
                       'https://youtu.be/Y__Ns7FS5lA', 'https://youtu.be/kD5ZDwdtJ10', 'https://youtu.be/W6A4DEr7XW4',
                       'https://youtu.be/Eao7VNpv1f0', 'https://youtu.be/y3Xu5o6Pxfg', 'https://youtu.be/qiUfLIbbedw',
                       'https://youtu.be/jzhetb1wJeM']},
            {'name': 'Уроки Python для начинающих', 'chan': 'https://www.youtube.com/channel/UCvuY904el7JvBlPbdqbfguw',
             'playlist': 'https://www.youtube.com/watch?v=n0xtO0x81cg&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu',
             'links': ['https://youtu.be/n0xtO0x81cg', 'https://youtu.be/_fDwlrrDkZc', 'https://youtu.be/Q7ccXmziG-I',
                       'https://youtu.be/j8AePyuLw38', 'https://youtu.be/tCSD-zNVkO4', 'https://youtu.be/6uSUQz3k_EM',
                       'https://youtu.be/ol23jnhVAOY', 'https://youtu.be/lFHwzZBweVg', 'https://youtu.be/NgQzna6il2w',
                       'https://youtu.be/NaA2H25gxN4']},
            {'name': 'Уроки С++ с нуля', 'chan': 'https://www.youtube.com/channel/UCvuY904el7JvBlPbdqbfguw',
             'playlist': 'https://www.youtube.com/watch?v=qSHP98i9mDU&list=PL0lO_mIqDDFXNfqIL9PHQM7Wg_kOtDZsW',
             'links': []},
            {'name': 'Telegram Bot на Python', 'chan': 'https://www.youtube.com/channel/UCvuY904el7JvBlPbdqbfguw',
             'playlist': 'https://www.youtube.com/watch?v=HodO2eBEz_8&list=PL0lO_mIqDDFUdlTc097-1A9IBchtJEggp',
             'links': []},
            {'name': 'Создание онтологий Protege', 'chan': 'https://www.youtube.com/channel/UCyrqcJoBGdEje5MlqmJgb7Q',
             'playlist': 'https://www.youtube.com/watch?v=VIpV-hVo3bY&list=PLMDuaURn3ViYuD2HLtf0u4WTTGRFS-dIN',
             'links': []},
            {'name': 'Нейронные сети на Python', 'chan': 'https://www.youtube.com/channel/UClJzWfGWuGJL2t-3dYKcHTA',
             'playlist': 'https://www.youtube.com/watch?v=nV7cI5zgOpk&list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh',
             'links': []},
            {'name': 'Проектирование информационных систем',
             'chan': 'https://www.youtube.com/channel/UCyrqcJoBGdEje5MlqmJgb7Q',
             'playlist': 'https://www.youtube.com/watch?v=FMXRHBbjg8Q&list=PLMDuaURn3VibR0KEhlr5UK5onB9_J1tGn',
             'links': []},
            {'name': 'Теория вероятностей и математическая статистика',
             'chan': 'https://www.youtube.com/channel/UCEEhbFAvl3fOW5geICQbMcg',
             'playlist': 'https://www.youtube.com/watch?v=pGVmzHfE3dY&list=PLthfp5exSWEqYroMZVPIOPd5Dz3ARAXzN',
             'links': []},
            {'name': 'Понятие информационных систем',
             'chan': 'https://www.youtube.com/channel/UCq2P8LO8PaEXxjv1sqts17Q',
             'playlist': 'https://www.youtube.com/watch?v=OylUNwtHyVM&list=PLset6wIBIRR1CCSG5vQkaUMqhXWOXo1GK',
             'links': []},
            {'name': 'Архетиктура компьютера и операционные системы',
             'chan': 'https://www.youtube.com/channel/UCEEhbFAvl3fOW5geICQbMcg',
             'playlist': 'https://www.youtube.com/watch?v=kKDAY-Xu-Mc&list=PLthfp5exSWEqs8WEh41MffNz6fu9wg_dx',
             'links': []},
            ]

basa = {'name': 'Базовый курс компьютерных сетей', 'chan': 'https://www.youtube.com/c/AndreySozykinCS/videos',
        'playlist': 'https://www.youtube.com/watch?v=OLFA0soYGhw&list=PLtPJ9lKvJ4oiNMvYbOzCmWy6cRzYAh9B1', 'links': []}
prod = {'name': 'Продвинутый курс компьютерных сетей', 'chan': 'https://www.youtube.com/c/AndreySozykinCS/videos',
        'playlist': 'https://www.youtube.com/watch?v=Y4l8ScRLrf4&list=PLtPJ9lKvJ4oh_w4_jtRnKE11aqeRldCFI', 'links': []}
prac = {'name': 'Практический курс компьютерных сетей', 'chan': 'https://www.youtube.com/c/TechAcad/playlists',
        'playlist': '', 'links': []}


class Film:
    def __init__(self):
        self.dur = None
        self.url = None
        self.descr = None
        self.id = None
        self.f_name = None

    def update(self, data):
        self.id = data[0]
        self.f_name = data[1]
        self.descr = data[2]
        self.url = data[3]
        self.dur = data[4]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global state
    file = open('init.sql', mode='r')
    cur = conn.cursor()
    sql = file.read()
    cur.executescript(sql)
    conn.commit()
    state = "begin"
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}")
    markup_reply = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text='Да', callback_data='Да')
    no = types.InlineKeyboardButton(text='Нет', callback_data='Нет')
    markup_reply.add(yes, no)
    bot.send_message(message.chat.id, "Хотите ли вы отдохнуть?", reply_markup=markup_reply)


def generate_film(username):
    cur = conn.cursor()
    cur.execute("SELECT * FROM films where films.id not in (select film_id from people_watch where p_name = ?);"
                , (username,))
    all_results = cur.fetchall()
    print(len(all_results))
    index = np.random.randint(len(all_results), size=1)
    conn.commit()
    cur_film.update(data=all_results[index[0]])


def filter_to_begin(_):
    global state
    if state != 'begin':
        return False
    return True


cur_film = Film()


@bot.callback_query_handler(func=filter_to_begin)
def callback_to_start(call):
    global state
    if call.data == 'Да':
        bot.send_message(call.message.chat.id, "Отлично, сейчас предложим вам фильм!")
        generate_film(call.from_user.username)
        bot.send_message(call.message.chat.id,
                         f"Название -- <b>{cur_film.f_name}</b>.\nДлительность -- <b>{cur_film.dur} мин</b>.\nОписание -- {cur_film.descr}.",
                         parse_mode='html')
        markup_reply = types.InlineKeyboardMarkup()
        yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        markup_reply.add(yes, no)
        state = 'question_for_watching'
        bot.send_message(call.message.chat.id, "Смотрели ли вы данный фильм?", reply_markup=markup_reply)
    else:
        markup_reply = types.InlineKeyboardMarkup()
        lst = []
        for ind, el in enumerate(channels):
            lst.append(types.InlineKeyboardButton(text=el['name'], callback_data=str(ind)))
        state = 'studying'
        markup_reply.add(*lst, types.InlineKeyboardButton(text='Компьютерные сети', callback_data='computer_networks'))
        bot.send_message(call.message.chat.id, "Выберете, чем вы бы хотели заняться:", reply_markup=markup_reply)


def filter_to_studying(call):
    global state
    if state != 'studying' or not call.data.isdigit():
        return False
    return True


@bot.callback_query_handler(func=filter_to_studying)
def callback_to_studying(call):
    global state
    ind = int(call.data)
    bot.send_message(call.message.chat.id, f"Канал -- {channels[ind]['chan']}")
    bot.send_message(call.message.chat.id, f"Плейлист занятий -- {channels[ind]['playlist']}")
    for index, link in enumerate(channels[ind]['links']):
        bot.send_message(call.message.chat.id, f"Урок номер {index + 1} -- {link}")
    state = 'before start'
    bot.send_message(call.message.chat.id, "Введите /start, чтобы начать заново")


def filter_for_networks(call):
    global state
    if state == 'studying' and call.data == 'computer_networks':
        return True
    return False


@bot.callback_query_handler(func=filter_for_networks)
def callback_to_networks(call):
    global state
    markup = types.InlineKeyboardMarkup()
    theory = types.InlineKeyboardButton(text='Теоритический трек', callback_data='thr')
    practice = types.InlineKeyboardButton(text='Практический трек', callback_data='prac')
    markup.add(theory, practice)
    state = 'track_checking'
    bot.send_message(call.message.chat.id, "Выберете трек обучения:", reply_markup=markup)


def filter_track(_):
    global state
    if state != 'track_checking':
        return False
    return True


@bot.callback_query_handler(func=filter_track)
def callback_to_networks(call):
    global state
    if call.data == 'thr':
        markup = types.InlineKeyboardMarkup()
        bas = types.InlineKeyboardButton(text='Базовый уровень', callback_data='bas')
        prods = types.InlineKeyboardButton(text='Продвинутый уровень', callback_data='prod')
        markup.add(bas, prods)
        state = 'networks_final'
        bot.send_message(call.message.chat.id, "Выберете уровень обучения:", reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, f"Канал -- {prac['chan']}")
        state = 'before start'
        bot.send_message(call.message.chat.id, "Введите /start, чтобы начать заново")


def filter_network_final(_):
    global state
    if state != 'networks_final':
        return False
    return True


@bot.callback_query_handler(func=filter_network_final)
def callback_to_networks(call):
    global state
    if call.data == 'bas':
        bot.send_message(call.message.chat.id, f"Канал -- {basa['chan']}")
        bot.send_message(call.message.chat.id, f"Плейлист занятий -- {basa['playlist']}")
    else:
        bot.send_message(call.message.chat.id, f"Канал -- {prod['chan']}")
        bot.send_message(call.message.chat.id, f"Плейлист занятий -- {prod['playlist']}")
    state = 'before start'
    bot.send_message(call.message.chat.id, "Введите /start, чтобы начать заново")


def filter_to_watching_film(_):
    global state
    if state != 'question_for_watching':
        return False
    return True


def save_watching(username):
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO people_watch values(?, ?);", (username, cur_film.id))
    conn.commit()


@bot.callback_query_handler(func=filter_to_watching_film)
def callback_to_start(call):
    global state
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "Оцените фильм от 1 до 10, пожалуйста:")
        state = 'estimation'
    else:
        markup = types.InlineKeyboardMarkup()
        but = types.InlineKeyboardButton(text='Посмотреть фильм', url=cur_film.url)
        markup.add(but)
        bot.send_message(call.message.chat.id, text="Хотели бы посмотреть данный фильм?", reply_markup=markup)
        state = 'before start'
        bot.send_message(call.message.chat.id, "Введите /start, чтобы начать заново")


def filter_to_est(_):
    global state
    if state != 'estimation':
        return False
    return True


@bot.message_handler(func=filter_to_est)
def estimation(message):
    global state
    if not message.text.isdigit() or int(message.text) < 1 or int(message.text) > 10:
        bot.send_message(message.chat.id, "Введите оценку от 1 до 10, пожалуйста:")
    else:
        bot.send_message(message.chat.id, f"Выставлена оценка -- <b>{int(message.text)}</b>", parse_mode='html')
        save_watching(message.from_user.username)
        bot.send_message(message.chat.id, "Введите /start, чтобы начать заново")
        state = 'before start'


bot.infinity_polling()

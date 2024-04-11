
import telebot
from telebot import types


#####################################

class Bot_inline_btns:
    def __init__(self):
        super(Bot_inline_btns, self).__init__()
        self.__markup = types.InlineKeyboardMarkup(row_width=1)

    def start_btns(self):
        reg = types.InlineKeyboardButton('ПОЛУЧИТЬ СИГНАЛ', callback_data='reg')
        self.__markup.add(reg)
        return self.__markup

    def reg_btns(self):
        site = types.InlineKeyboardButton('САЙТ', url='https://1wnurc.com/?open=register#cpk2')
        check = types.InlineKeyboardButton('Я ЗАРАГЕСТИРОВАЛСЯ!', callback_data='checkreg')
        self.__markup.add(site, check)
        return self.__markup

    def ok_btns(self):
        site = types.InlineKeyboardButton('САЙТ', url='https://1wnurc.com/?open=register#cpk2')
        ready = types.InlineKeyboardButton('ПРОВЕРИТЬ РЕГИСТРАЦИЮ', callback_data='okk')
        self.__markup.add(site, ready)
        return self.__markup

    def cost_btns(self):
        cost = types.InlineKeyboardButton('УЗНАТЬ СТОИМОСТЬ', callback_data='checkcost')
        self.__markup.add(cost)
        return self.__markup
    def podpiska_btns(self):
        pay = types.InlineKeyboardButton('ОПЛАТИТЬ', callback_data='pay')
        self.__markup.add(pay)
        return self.__markup

    def manager_btns(self):
        accept = types.InlineKeyboardButton('Подтвердить!', callback_data='accept')
        deny = types.InlineKeyboardButton('Отклонить!', callback_data='deny')
        self.__markup.add(accept, deny)
        return self.__markup

    def pay_btns(self):
        oplata = types.InlineKeyboardButton('Я ОПЛАТИЛ!', callback_data='oplata')
        self.__markup.add(oplata)
        return self.__markup

    def sid_btns(self):
        sid = types.InlineKeyboardButton('ПОЛУЧИТЬ СИД', callback_data='sid')
        self.__markup.add(sid)
        return self.__markup

    def changesid_btns(self):
        change = types.InlineKeyboardButton('ПОДТВЕРДИТЬ ИЗМЕНЕНИЕ СИДА', callback_data='changesid')
        self.__markup.add(change)
        return self.__markup

    def next_btns(self):
        check_game = types.InlineKeyboardButton('ПРОВЕРИТЬ ИГРУ', callback_data='checkgame')
        next_signal = types.InlineKeyboardButton('ПОЛУЧИТЬ СИГНАЛ', callback_data='signal')
        self.__markup.add(check_game, next_signal)
        return self.__markup
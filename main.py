config_name = 'secrets.json'
group_id = -1001998277120

import os
import telebot
import platform
import random
from threading import Lock
from config_parser import ConfigParser
from frontend import Bot_inline_btns
from backend import TempUserData, DbAct
from db import DB


def select_message(messages, weights):
    return random.choices(messages, weights=weights, k=1)[0]


def main():
    @bot.message_handler(commands=['start'])
    def start_msg(message):
        buttons = Bot_inline_btns()
        user_id = message.chat.id
        db_actions.add_user(user_id, message.from_user.first_name, message.from_user.last_name,
                            f'@{message.from_user.username}')
        bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}!\n\n'
                                          'Я Бот игры Lucky Jet🚀', reply_markup=buttons.start_btns())

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        buttons = Bot_inline_btns()
        user_id = call.message.chat.id

        if call.data == 'signal':
            x = round(random.uniform(1.20, 2.50), 2)
            bot.send_message(call.message.chat.id, f'Сигнал: {x}x', reply_markup=buttons.next_btns())

        elif call.data == 'reg':
            bot.send_message(call.message.chat.id, '📲 Шаг №1. Регистрация.\n\n'
                                                   '✦ Для синхронизации с ботом необходимо зарегистрировать НОВЫЙ АККАУНТ на 1WIN по ранее неиспользованному номеру телефона и почте по кнопке «Регистрация» ниже👇\n\n'
                                                   '🎁 При регистрации указать ПРОМОКОД: 𝐏𝐑𝐎𝐌𝐎𝐒𝐓𝐀𝐑𝐓 для получения бонусов и избежания блокировок при использовании Бота.\n\n'
                                                   '❗️ Убедитесь, что Вы вышли со старого аккаунта и при регистрации указали промокод.\n\n'
                                                   '📌По всем ❓ писать на почту ➡️ foreverchampi0n@inbox.ru',
                             reply_markup=buttons.reg_btns())

        elif call.data == 'checkreg':
            bot.send_message(call.message.chat.id, '💰 Шаг №2. Пополнение аккаунта.\n\n'
                                                   f'💳Чтобы получать сигналы и заработать тебе осталось пополнить свой новый аккаунт 1WIN и проверить регистрацию по кнопке ниже. 🔎\n\n'
                                                   f'🤖Минимальная сумма пополнения от 500₽\n\n'
                                                   f'💸По нашему промокоду: 𝐏𝐑𝐎𝐌𝐎𝐒𝐓𝐀𝐑𝐓 получи приветственный бонус +500% на первый депозит! (если депозит 1000₽ Вам начислится 5000₽)\n\n'
                                                   f'🚫Если условия не будут выполнены, Бот не выдаст сигналы',
                             reply_markup=buttons.ok_btns())

        elif call.data == 'okk':
            bot.send_message(call.message.chat.id, 'Хорошо! Теперь ты можешь приобрести ключ к сигналам Lucky Jet🚀\n\n'
                                                   'Для того чтобы узнать стоимость ключа нажми на кнопку «Узнать стоимость» ниже👇',
                             reply_markup=buttons.cost_btns())

        elif call.data == 'checkcost':
            bot.send_message(call.message.chat.id, '🗝️Стоимость ключа на данный момент оценивается в 27$ (2490₽).\n\n'
                                                   '♾️Ключ можно приобрести навсегда\n\n'
                                                   '💸Покупка ключа гарантирует Вам хороший заработок за счёт сигналов Lucky Jet\n\n'
                                                   '⚠️Бот выдаёт точные сигналы на каждый раунд игры',
                             reply_markup=buttons.podpiska_btns())

        elif call.data == 'pay':
            bot.send_message(call.message.chat.id, '💸 Реквизиты для оплаты 💸\n\n'
                                                   'По номеру карты: <code>5599 0020 6815 5748</code>',
                             reply_markup=buttons.pay_btns(), parse_mode='HTML')
        elif call.data == 'oplata':
            bot.send_message(call.message.chat.id, 'Пришли мне информацию, от кого должен поступить платеж!\n\n'
                                                   'Я проверю информацию и подтвержу платеж в течении нескольких минут!')
            temp_user_data.temp_data(user_id)[user_id][0] = 1
        elif call.data == 'accept':
            bot.send_message(chat_id=db_actions.get_user_id_from_topic(call.message.reply_to_message.id), text='Оплата принята!\n\n'
                                      'Можете начать получать сигналы!', reply_markup=buttons.sid_btns())
        elif call.data == 'deny':
            bot.send_message(db_actions.get_user_id_from_topic(call.message.reply_to_message.id), 'Оплата не принята! Попробуйте еще раз!')
        elif call.data == 'sid':
            bot.send_message(call.message.chat.id, 'Ваш персональный сид - 7yJmf289TJ-QWTIE-h7C\n\n'
                                                   'Смотрите как активировать сид в моём ТГ канале — https://t.me/+LXCXIM_BmNo0ODFi', reply_markup=buttons.changesid_btns())
        elif call.data == 'changesid':
            bot.send_message(call.message.chat.id, '⚠️Перед получением сигнала нажми кнопку «ПРОВЕРИТЬ ИГРУ» для того, чтобы бот выбрал более благоприятный вариант для выдачи сигнала.\n\n'
                                                   '❌Это поможет избежать краша на 1.00х', reply_markup=buttons.next_btns())
        elif call.data == 'checkgame':
            y = 'Пережди 1 игру📛'
            t = 'Пережди 2 игры📛'
            z = 'Ставь✅'
            messages = [y, t, z]
            weights = [10, 10, 80]
            selected_message = select_message(messages, weights)
            bot.send_message(call.message.chat.id, selected_message)

    @bot.message_handler(content_types=['text', 'photo'])
    def text_message(message):
        buttons = Bot_inline_btns()
        user_input = message.text
        user_id = message.chat.id
        code = temp_user_data.temp_data(user_id)[user_id][0]
        if code == 1:

            topic_id = telebot.TeleBot.create_forum_topic(bot, chat_id=group_id,
                                                          name=f'{message.from_user.first_name} '
                                                               f'{message.from_user.last_name} ПОПОЛНЕНИЕ БАЛАНСА',
                                                          icon_color=0x6FB9F0).message_thread_id
            bot.forward_message(chat_id=group_id, from_chat_id=message.chat.id, message_id=message.id,
                                message_thread_id=topic_id)
            db_actions.update_review_id(user_id, topic_id)
            bot.send_message(chat_id=group_id, message_thread_id=topic_id, text='Получена оплата!✅\n'
                                                                                'Проверьте информацию и '
                                                                                'подтвердите!',
                             reply_markup=buttons.manager_btns())
            bot.send_message(user_id, 'Ваша заявка принята, ожидайте!')

    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    temp_user_data = TempUserData()
    db = DB(config.get_config()['db_file_name'], Lock())
    db_actions = DbAct(db)
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()

#to do - webhooks
#clean up
#buttons


import config
import telebot
import dbworker
import pandas
import time

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    #bot.send_message(message.chat.id, "Type ENG for english version; введите - РУ для русской версии")
    bot.send_message(message.chat.id, "Введите - РУ для русской версии")
    dbworker.set_state(message.chat.id, config.States.S_LANG_SELECT.value)

# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    #bot.send_message(message.chat.id, "New game. Type ENG for english version; введите - РУ для русской версии")
    bot.send_message(message.chat.id, "Введите - РУ для русской версии")
    #bot.send_message(message.chat.id, config.States.S_LANG_SELECT.value)
    dbworker.set_state(message.chat.id, config.States.S_LANG_SELECT.value)

@bot.message_handler(content_types=["text"])
def game_run(message):
    state = dbworker.get_current_state(message.chat.id)
    #bot.send_message(message.chat.id, state)
    if state == config.States.S_START.value:
        #bot.send_message(message.chat.id, "New game. Type ENG for english version; введите - РУ для русской версии")
        bot.send_message(message.chat.id, "Введите - РУ для русской версии")
        dbworker.set_state(message.chat.id, config.States.S_LANG_SELECT.value)
        return
    action = message.text
    if state == config.States.S_LANG_SELECT.value:
        #if action in ('ENG', 'РУ'):
        if action in ('РУ'):
            if action == 'ENG':
                dbworker.set_state(message.chat.id, config.States.S_BRANCH_0_1_ENG.value)
                reply, actions = get_reply(config.States.S_BRANCH_0_1_ENG.value)
                #bot.send_message(message.chat.id, reply)
                #bot.send_message(message.chat.id, actions)
                send_message(message,reply, actions)
                return
            else:
                dbworker.set_state(message.chat.id, config.States.S_BRANCH_0_1_RU.value)
                #state = dbworker.get_current_state(message.chat.id)
                #bot.send_message(message.chat.id, state)
                reply, actions = get_reply(config.States.S_BRANCH_0_1_RU.value)
                #bot.send_message(message.chat.id, reply)
                #bot.send_message(message.chat.id, actions)
                send_message(message,reply, actions)
                return
        else:
            #reply = "You've entered incorrect value / Вы ввели неверное значение"
            reply = "Я вас не понимаю"
            bot.send_message(message.chat.id, reply)
            return
    if (state == config.States.S_BRANCH_END_1_RU.value) or (state == config.States.S_BRANCH_END_9_RU.value) or \
        (config.States.S_BRANCH_END_10_RU == "branch_1_10_ru") or \
            (config.States.S_BRANCH_END_11_RU == "branch_1_11_ru"):
        reply = 'Это офицер Джонсон. Мы нашли тело вашего друга недалеко от дома Поттеров. Приезжайте на опознание'
        bot.send_message(message.chat.id, reply)
        bot.send_message(message.chat.id, 'Чтобы начать сначала введите /reset')
        return
    if state == config.States.S_BRANCH_END_2_RU.value:
        reply = 'Вы знаете, хорошо, что я послушал вас и не стал переживать по поводу Эндрю. Эндрю - отличный парень.' \
                ' Кстати,' \
                'Аркхем замечательный город. Приезжайте ко мне.'
        bot.send_message(message.chat.id, reply)
        reply = 'Ктулху Фтагн!'
        bot.send_message(message.chat.id, reply)
        bot.send_message(message.chat.id, 'Чтобы начать сначала введите /reset')
        return
    if state == config.States.S_BRANCH_END_3_RU.value:
        reply = 'Вы знаете, хорошо, что я послушал вас и не стал переживать по поводу Эндрю. Я так хорошо отдохнул.' \
                'Ждите меня скоро в Чикаго!'
        bot.send_message(message.chat.id, reply)
        bot.send_message(message.chat.id, 'Чтобы начать сначала введите /reset')
        return
    if (state == config.States.S_BRANCH_END_4_RU.value) or (state == config.States.S_BRANCH_END_7_RU.value):
        reply = 'Приезжайте на ферму к Эндрю.' \
                'Здесь свежий воздух и отличные перспективы!'
        bot.send_message(message.chat.id, reply)
        bot.send_message(message.chat.id, 'Чтобы начать сначала введите /reset')
        return
    if state == config.States.S_BRANCH_END_5_RU.value:
        reply = 'Давайте, встретимся сегодня, я вернулся в Чикаго'
        bot.send_message(message.chat.id, reply)
        bot.send_message(message.chat.id, 'Чтобы начать сначала введите /reset')
        return
    if (state == config.States.S_BRANCH_END_6_RU.value) or (state == config.States.S_BRANCH_END_8_RU.value):
        bot.send_message(message.chat.id, 'Чтобы начать сначала введите /reset')
        return
    else:
        options, next_states = get_possible_options(state)
        if action in options:
            next_state = next_states[int(action)-1][4:len(next_states[int(action)-1])]
            dbworker.set_state(message.chat.id, next_state)
            reply, actions = get_reply(next_state)
            send_message(message,reply, actions)
            return
            #reply = reply.split(',')
            #bot.send_message(message.chat.id, reply[-2])
            #for i in range(0,len(reply)):
            #    bot.send_message(message.chat.id, reply[i])
            #    time.sleep(5)
            #bot.send_message(message.chat.id, actions)
        else:
            reply = "Я вас не понимаю"
            bot.send_message(message.chat.id, reply)
            return

def send_message(message,reply, actions):
    for i_message in reply:
        bot.send_message(message.chat.id, i_message)
        time.sleep(1)
    bot.send_message(message.chat.id, actions)

def get_reply(current_state):
    quest_db = pandas.read_csv(config.quest_db, sep=';', header=None, index_col=0)
    reply = quest_db.loc[current_state][1].split('.')
    actions = quest_db.loc[current_state][2]
    return reply, actions

def get_possible_options(current_state):
    quest_db = pandas.read_csv(config.quest_db, sep=';', header=None, index_col=0)
    options = quest_db.loc[current_state][4].split(',')
    next_states = quest_db.loc[current_state][3].split(',')
    return options, next_states

if __name__ == '__main__':
    bot.polling(none_stop=True)

import telebot
from password import gen_pass 
from rulet import shot
import random


bot = telebot.TeleBot("")
free = 7

users = {}
us_ans = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. \n /hello - поздороваться \n /bye - попрощаться \n /newpassword (кол-во символов в пароле) - сгенерировать пароль \n /rulet - поиграть в русскую рулетку \n /heh (кол-во 'heh') - похехекать \n /dice (кол-во граней)(кол-во бросков) - кинуть дайс \n /spam (текст спама)(кол-во сообщений) - заспамить")
    free = 7
@bot.message_handler(commands=['hello', 'hi'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['newpassword'])
def send_pass(message):
    words = message.text.split()
    if len(words) < 2 :
        bot.reply_to(message, gen_pass(10))
    else:
        lenght = int(words[1])
        bot.reply_to(message, gen_pass(lenght))

@bot.message_handler(commands=['dice'])
def send_dice(message):
    words = message.text.split()
    if len(words) < 2 :
        bot.reply_to(message, "Недостаточно данных")
    else:
        for i in range(int(words[2])):
            result = random.randint(1 , int(words[2]))
            bot.reply_to(message, result)
            


@bot.message_handler(commands=['spam'])
def send_spam(message):
    words = message.text.split()
    if len(words) < 3 :
        bot.reply_to(message, "Недостаточно данных")
    else:
        text = ""
        w = words[ 1:len(words)-1]
        for i in w:
            text += i + ""
        for i in range (int(words[-1])):
            bot.reply_to(message, text)
            
        
             
            
    


@bot.message_handler(commands=['rulet'])
def send_shot(message):
    global free 
    life = shot(free)
    free -= 1
    if life:
        if free != 1 :          
            bot.reply_to(message, "вы пережили пулю")
        elif free == 1 :
            bot.reply_to(message, "вы пережили все пули")
            free = 7
    else:
        bot.reply_to(message, "вы не пережили пулю")
        free = 7

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
















@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()





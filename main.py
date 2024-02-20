import telebot
import random
import requests
from user_agent import generate_user_agent

token = "6939044877:AAEFoD_J04mooSwYnBQiVpWfg4BzwDEMb8Y"
bot = telebot.TeleBot(token)
# @ICTS_930
headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
'User-Agent': generate_user_agent(),
}

@bot.message_handler(commands=['start'])
def Welcome(message):
	bot.reply_to(message,'مرحبا بك في بوت صيد يوزرات مميزه تام تام',reply_markup=telebot.types.InlineKeyboardMarkup([
        [telebot.types.InlineKeyboardButton(text='بدأ', callback_data='start')]
    ]))
    
@bot.callback_query_handler(lambda call: call.data == "start")
def TamTa(call):
    good = 0
    bad = 0
    while True:
        a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        aa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        aaa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        hel = str("".join(random.choice(a)for x in range(1)))
        era = str("".join(random.choice(aa)for x in range(1)))
        wel = str("".join(random.choice(aaa)for x in range(1)))
        user = wel+wel+wel+hel+wel
        
        req = requests.get(f'https://tt.me/{user}',headers=headers).text
        if '<meta property="og:url" content="https://tamtam.chat/">' in req:
            good += 1
            bot.send_message(call.message.chat.id,f'done: {user}')
        else:
            bad += 1
            print('\033[0;31m',user)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"user: {user}\n\ndone: {good}\n\nbad: {bad}")
 
bot.polling(True)
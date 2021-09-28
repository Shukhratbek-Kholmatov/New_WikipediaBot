import telebot
from telebot import types
import wikipedia
from search_wiki import search
from button_maker import make_button
admin="904185120"
from config import token
bot=telebot.TeleBot(token,parse_mode="MARKDOWN")
@bot.message_handler(commands=["start"])
def start(message):
    user=message.from_user
    main_button=make_button("main_button")
    bot.send_message(message.chat.id,f"*•Tilni tanlang.\n•Choose language.\n•Выберите язык.*",reply_markup=main_button)
    if format(user.username)!=None:
        bot.send_message(admin,f"*@{format(user.username)}\ntomonidan /start bosildi.\nID:\n{message.chat.id}*")
    else:
        bot.send_message(admin,f"*{format(user.first_name)}\ntomonidan /start bosildi.\nID:\n{message.chat.id}**")
@bot.message_handler(commands=["info"])
def info(message):
    button1=make_button("button1")
    button2=make_button("button2")
    button3=make_button("button3")
    try:
        with open(f"user_info/{message.chat.id}.txt") as detect:
            read=detect.readlines()
            if "Uz" in read:
                bot.send_message(message.chat.id,f"*Ushbu bot orqali siz wikipediadan istalgan ma'lumotni qidirishingiz mumkin.Shunchaki botga qidirilishi kerak bo'lgan matnni yuboring,bot esa sizga u haqida kerakli maqolani  yuboradi.*",reply_markup=button1)
            elif "Eng" in read:
               bot.send_message(message.chat.id,f"*With this bot you can search information which in wikipedia.Just send the bot a text which need to search,the bot will send the text to you.*",reply_markup=button2)
            elif "Ru" in read:
               bot.send_message(message.chat.id,f"*Отправыте мне текст,я отправлю информация о твой текст.*",reply_markup=button3)
    except:
        bot.send_message(message.chat.id,f"*•Tilni tanlang.\n•Choose language.\n•Выберите язык.*")
@bot.message_handler(commands=["dev"])
def dev(message):
    button1=make_button("button1")
    button2=make_button("button2")
    button3=make_button("button3")
    try:
                with open(f"user_info/{message.chat.id}.txt") as detect:
                    read=detect.readlines()
                    if "Uz" in read:
                        bot.send_message(message.chat.id,f"*Bot dasturchisi:\n@shukhrat_2602*",reply_markup=button1)
                    elif "Eng" in read:
                       bot.send_message(message.chat.id,f"*Developer of this bot:\n@shukhrat_2602*",reply_markup=button2)
                    elif "Ru" in read:
                       bot.send_message(message.chat.id,f"*Програмист бота:\n@shukhrat_2602*",reply_markup=button3)
    except:
                 bot.send_message(message.chat.id,f"*•Tilni tanlang.\n•Choose language.\n•Выберите язык.*")
                 
                 
@bot.message_handler(content_types=["text"])
def text(message):
    user=message.from_user
    mid=message.chat.id
    msg=message.text
    main_button=make_button("main_button")
    button1=make_button("button1")
    button2=make_button("button2")
    button3=make_button("button3")
    bot.send_chat_action(mid,"typing")
    if msg=="🇺🇿Uz":
                with open(f"user_info/{mid}.txt","w") as choice:
                    choice.write("Uz")
                    bot.reply_to(message,f"*Assalomu alaykum* _{format(user.first_name)}._\n*Menga matn yuboring,men unga oid ma'lumotni yuboraman.*",reply_markup=button1)
    elif msg=="🇬🇧Eng":
                            with open(f"user_info/{mid}.txt","w") as choice:
                                choice.write("Eng")
                                bot.reply_to(message,f"*Hello* _{format(user.first_name)}_.\n*Send me a text.I'll send information about your text.*", reply_markup=button2)
    elif msg=="🇷🇺Ru":
                                        with open(f"user_info/{mid}.txt","w") as choice:
                                            choice.write("Ru")
                                            bot.reply_to(message,f"*Здравствуйте* _{format(user.first_name)}._\n*Отправыте мне текст,я отправлю информация о твой текст.*",reply_markup=button3)
    elif msg!="🇺🇿Uz" and msg!="🇬🇧Eng" and msg!="🇷🇺Ru":
           try:
               with open(f"user_info/{mid}.txt","r") as detect:
                   read=detect.readlines()
                   if "Uz" in read:
                           response=search("Uz",msg)
                           bot.reply_to(message,f"*{response}*",reply_markup=button1)
                   elif "Eng" in read:
                        response=search("Eng",msg)
                        bot.reply_to(message,f"*{response}*",reply_markup=button2)
                       
                   elif "Ru" in read:
                            response=search("Ru",msg)
                            bot.reply_to(message,f"*{response}*",reply_markup=button3)
           except:
               bot.reply_to(message,f"*•Tilni tanlang.\n•Choose language.\n•Выберите язык.*",reply_markup=main_button)

bot.polling()                             
                             
                    



import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080',
    "urllib3_proxy_kwargs": {"username": "learn", "password": "python"}}

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет пользователь")
    #print(update) - печатает в консоли данные о чате , пользователе

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater("5032920236:AAEhV6Fq6XzjBba9KHGycs-nnBPALT3m59g", use_context = True, request_kwargs = PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot Startoval")
    mybot.start_polling()
    mybot.idle()

main()
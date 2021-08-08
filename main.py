import telebot
from selenium import webdriver



Token = "1870752405:AAFbA6dtbmClymaxYwleykaU9KC3W2_VyRg"

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def First(message):
    reply = telebot.types.ReplyKeyboardMarkup(True)
    reply.row("Lumos", "Nox")
    bot.send_message(message.chat.id, "Готов к работе!", reply_markup=reply)

@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text.lower() == "lumos":

        driver = webdriver.Chrome()
        driver.get('192.168.1.13')
        element = driver.find_elements_by_link_text("here")[0].click()

        bot.send_message(message.chat.id, "Зажигаю")
    if message.text.lower() == "nox":

        driver = webdriver.Chrome()
        driver.get('192.168.1.13')
        element = driver.find_elements_by_link_text("here")[1].click()

        bot.send_message(message.chat.id, "Тушу свет")


bot.polling(none_stop=True)

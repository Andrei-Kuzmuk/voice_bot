import os
import settings
import telebot
import voice


bot = telebot.TeleBot(settings.api_key, threaded=False)
language = ["en"]


# Функция для обработки команды /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я эхо-бот. Напиши мне что-нибудь!")


@bot.message_handler(commands=["en", "ru"])
def _relanguage(message):
    language[0] = message.text[1:]
    bot.send_message(message.chat.id, f"вы переключились на язык {language[0]}")


# Функция для обработки текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all_audio(message):
    voice.text_to_speech(message.text, "voice.mp3", language[0])
    with open("voice.mp3", "rb") as file:
        bot.send_audio(message.chat.id, file)


if __name__ == "__main__":
    bot.polling()

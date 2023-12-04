import telebot


class Bot:
    def __init__(self, token):
        self.token = token
        self.bot = telebot.TeleBot(token)

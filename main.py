from dotenv import load_dotenv

import os

import bot

if __name__ == '__main__':
    load_dotenv()
    token = os.getenv()

    bot.Bot(token)

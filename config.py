from aiogram import Bot, Dispatcher
from decouple import config


sozdatel=632308366
TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
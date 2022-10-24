import aioschedule
from aiogram import types,Dispatcher
from config import bot
import asyncio


async def get_chat_id(message:types.Message):
    global chat_id
    chat_id=message.from_user.id
    await message.answer("Вы не пропустите выход новых серий!")

async def new_monday():
    await bot.send_message(chat_id=chat_id, text="Вышла новая серия сериала!")

async def new_friday():
    await bot.send_message("Вышла новая серия аниме!")

async def scheluder():
    aioschedule.every().monday.at('18:17').do(new_monday)
    aioschedule.every().friday.at('19:00').do(new_friday)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: "напомни" in word.text)

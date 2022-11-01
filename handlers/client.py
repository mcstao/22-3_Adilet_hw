from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from parsers.fonar import parser
from keyboards.client_kb import start_markup
import random
from database.bot_db_mentor import sql_command_random_mentors


async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Приветствую вас {message.from_user.first_name}!",
                           reply_markup=start_markup)


async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Разбирайся сам!")


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Какой безалкогольный напиток первым был взят в космос?"
    answers = [
        "PEPSI",
        "COLA",
        "FANTA",
        "SPRITE"
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="изи же",
        open_period=10,
        reply_markup=markup
    )


async def mem(message:types.Message):
    photos = ["media/1.jpg","media/2.jpg" , "media/3.jpg" ,"media/4.jpg" , "media/5.jpg","media/6.jpg","media/7.jpg"]
    photo = open(random.choice(photos),"rb")
    await bot.send_photo(message.chat.id,photo=photo)

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("Надо ответить на сообщение")


async def get_random_user(message: types.Message):
    await sql_command_random_mentors(message)


async def parser_fonar(message: types.Message):
    items = parser()
    for item in items:
        await message.answer(
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"{item['price']}"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'info'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(mem,commands=['mem'])
    dp.register_message_handler(pin,commands=['pin'],commands_prefix='!')
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(parser_fonar, commands=['fonar'])
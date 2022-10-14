from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

from config import bot, dp,sozdatel
import logging


@dp.message_handler(commands=['start', 'info'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Приветствую вас {message.from_user.first_name}!")


@dp.message_handler(commands=["mem"])
async def mem(message:types.Message):

    photos = ["media/1.jpg","media/2.jpg" , "media/3.jpg" ,"media/4.jpg" , "media/5.jpg","media/6.jpg","media/7.jpg"]
    photo = open(random.choice(photos),"rb")
    await bot.send_photo(message.chat.id,photo=photo)


@dp.message_handler(commands=['quiz'])
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
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="изи же",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Какой национальный вид спорта Канады?"
    answers = [
        "Футбол",
        "Баскетбол",
        "Хоккей",
        "Лакросс"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="изи же",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def quiz_3(call: types.CallbackQuery):
    question = "Какая страна является самой маленькой в мире?"
    answers = [
        "Мальта",
        "Мальдивы",
        "Ватикан",
        "Монако"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="изи же",
        open_period=10,
    )


@dp.message_handler()
async def echo(message: types.Message):

    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) * int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)
    await bot.forward_message(sozdatel, message.from_user.id, message.message_id)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
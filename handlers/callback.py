from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from database.bot_db_mentor import sql_command_delete_mentors


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
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="изи же",
        open_period=10,
        reply_markup=markup
    )



async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data='button_call_3')
    markup.add(button_call_3)
    question = "Какая страна является самой маленькой в мире?"
    answers = [
        "Мальта",
        "Мальдивы",
        "Ватикан",
        "Монако"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="изи же",
        open_period=10,
        reply_markup=markup
    )

async def quiz_4(call: types.CallbackQuery):

    question = "Что есть у кенгуру?"
    answers = [
        "Барсетка",
        "Чемодан",
        "Сумка",
        "Чехол"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="изи же",
        open_period=10
    )


async def complete_delete_mentors(call: types.CallbackQuery):
    await sql_command_delete_mentors(call.data.replace('delete ', ''))
    await call.answer(text='Стерт с базы данных!', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
    dp.register_callback_query_handler(quiz_4, lambda call: call.data == 'button_call_3')
    dp.register_callback_query_handler(
        complete_delete_mentors,
        lambda call: call.data and call.data.startswith("delete ")
    )
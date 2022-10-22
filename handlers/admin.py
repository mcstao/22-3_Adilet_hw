from aiogram import types, Dispatcher
from config import bot, dp, ADMINS

from database.bot_db_mentor import sql_command_all_mentors,sql_commands_get_all_id_mentors
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def kick(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id not in ADMINS:
            await message.reply("У вас нет  права на это")
        elif not message.reply_to_message:
            await message.reply("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан "
                                 f"кикнул участника {message.reply_to_message.from_user.full_name}")
    else:
        await message.reply("Пиши в группе!")






async def delete_data_mentors(message: types.Message):
    if not message.from_user.id in ADMINS:
        await message.reply("Ты не мой босс!")
    else:
        users = await sql_command_all_mentors()
        for user in users:
            await bot.send_message(message.chat.id,
                                    text=f"{user[1]}, {user[3]}, {user[2]}, "
                                         f"{user[4]}\n\n{user[0]}",
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(f"Delete {user[1]}", callback_data=f"delete {user[0]}")
                                 ))



async def distribution_mentors(message: types.Message):
    if not message.from_user.id in ADMINS:
        await message.reply("Ты не мой босс!")
    else:
        result = await sql_commands_get_all_id_mentors()
        for user_id in result:
            await bot.send_message(user_id[0], message.text[3:])


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(kick, commands=['kick'], commands_prefix='!/')
    dp.register_message_handler(distribution_mentors, commands=['R'])
    dp.register_message_handler(delete_data_mentors, commands=['del'])
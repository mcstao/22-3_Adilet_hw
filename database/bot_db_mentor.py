import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print("База данных менторов подключена!")

    db.execute(
        "CREATE TABLE IF NOT EXISTS MENTORS "
        "(ID INTEGER, name TEXT, direction TEXT, "
        "age INTEGER, groups TEXT)"
    )
    db.commit()

async def sql_command_insert_mentors(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO MENTORS VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_random_mentors(message):
    result = cursor.execute("SELECT * FROM MENTORS").fetchall()
    random_user = random.choice(result)
    await bot.send_message(message.chat.id,text=
                            f"{random_user[1]}, {random_user[3]}, {random_user[2]}, "
                                 f"{random_user[4]}\n\n{random_user[0]}")

async def sql_command_all_mentors():
    return cursor.execute('SELECT * FROM MENTORS').fetchall()


async def sql_command_delete_mentors(id):
    cursor.execute("DELETE FROM MENTORS WHERE id = ?", (id,))
    db.commit()


async def sql_commands_get_all_id_mentors():
    return cursor.execute('SELECT id FROM MENTORS').fetchall()
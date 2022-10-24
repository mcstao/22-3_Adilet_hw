import asyncio

from aiogram.utils import executor

from config import dp
import logging

from handlers import client,admin,callback,fsmAdminMentor,extra,notifications
from database.bot_db_mentor import sql_create

async def on_startup(_):
    asyncio.create_task(notifications.scheluder())
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
notifications.register_handlers_notifications(dp)
fsmAdminMentor.register_handlers_fsmAdminMentor(dp)

extra.register_handlers_extra(dp)




if __name__ ==  "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
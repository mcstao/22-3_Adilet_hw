from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State,StatesGroup

from config import bot,ADMINS
from keyboards.client_kb import cancel_markup,submit_markup
from database.bot_db_mentor import sql_command_insert_mentors


class FSMAdmin(StatesGroup):
    ID = State()
    name = State()
    direction = State()
    age = State()
    groups = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id not in ADMINS:
            print("Вы не куратор!")
        else:
            await FSMAdmin.ID.set()
            await message.answer(f"Приветствую {message.from_user.full_name}\n"
                                 f"Сгенерируйте ID ментора",
                                 reply_markup=cancel_markup)
    else:
        await message.answer('Пиши в личку!')

async def load_ID(message:types.Message, state=FSMContext):

    async with state.proxy() as data:
        data['ID'] =int(message.text)
    await FSMAdmin.next()
    await message.answer("Как зовут ментора?")

async def load_name(message:types.Message,state = FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какое направление?")

async def load_direction(message:types.Message,state = FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Сколько лет?")

async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await FSMAdmin.next()
    await message.answer("Какая группа?")

async def load_groups(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['groups'] = message.text
        await message.answer(f"Имя:{data['name']},Возраст: {data['age']}, Направление:{data['direction']}, "
                                       f"Группа:{data['groups']}\n\nID:{data['ID']}")
    await FSMAdmin.next()
    await message.answer("Все правильно?", reply_markup=submit_markup)

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert_mentors(state)
        await state.finish()
        await message.answer("Регистрация завершена")
    if message.text.lower() == 'нет':
        await state.finish()
        await message.answer("Отмена")

async def cancel_reg(message: types.Message, state: FSMContext):
    curren_state = await state.get_state()
    if curren_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты!")

def register_handlers_fsmAdminMentor(dp:Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start,commands=['mentors'])
    dp.register_message_handler(load_ID, state=FSMAdmin.ID)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_groups, state=FSMAdmin.groups)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
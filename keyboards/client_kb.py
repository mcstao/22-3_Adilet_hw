from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
help_button = KeyboardButton("/help")

location_button = KeyboardButton('Share location', request_location=True)
info_button = KeyboardButton('Share info', request_contact=True)

start_markup.add(start_button, quiz_button, help_button).add(location_button, info_button)


gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

gender_g = KeyboardButton("Девушка")
gender_b = KeyboardButton("Мальчик")
gender_u = KeyboardButton("Незнаю")

gender_markup.add(gender_g, gender_b, gender_u).add(KeyboardButton('CANCEL'))


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))


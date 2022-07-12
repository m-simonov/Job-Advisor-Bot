from aiogram import types
from services.users import UsersService
from main import bot, dp
from database import Session
from tables import Users


@dp.message_handler(commands=['start'])
async def send_hello_message(message: types.Message):
    tg_id = message.from_user.id
    username = message.from_user.username
    name = message.from_user.first_name

    service = UsersService()
    service.create(tg_id, username, name)
    await message.answer(text='Hello')


@dp.message_handler(commands=['users'])
async def get_users(message: types.Message):
    service = UsersService()
    users = service.get_list()
    await message.answer(text=users)

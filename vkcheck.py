from aiogram import Bot, types
from aiogram import executor
from aiogram import Dispatcher
from vk_api import VkApi
from vk_api.exceptions import BadPassword
import json, requests
from os import remove

TOKEN = ""
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_msg(message: types.Message):
    await message.answer("Введите логин:пароль от вконтакте для проверки!")


@dp.message_handler(content_types=["text"])
async def get_data(message: types.Message):
    raw_data = message.text
    try:
        phone = raw_data.split(":")[0]
        password = raw_data.split(":")[1]
    except IndexError:
        await message.reply("Введите логин:пароль от вконтакте для проверки!")
    vk_session = VkApi(f"{phone}", "{password}")
    try:
        vk_session.auth()
        vk = VK.get_api()
    except BadPassword:
        await message.reply("Невалид❌")
    else:
        await message.reply("Валид✅")


if __name__ == "__main__":
    executor.start_polling(dp)

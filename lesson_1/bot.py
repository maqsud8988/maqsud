import os
from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

# Bot yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    user_id = message.from_user.id
    user_name = message.from_user.username


    await message.reply("Assalomu alaykum! Botimizga xush kelibsiz.")


@dp.message_handler(commands=['data'])
async def send_data(message: types.Message):
    user_id = message.from_user.id

    user_info = get_user_info(user_id)

    if user_info is None:
        await message.reply("Sizning ma'lumotlaringiz topilmadi.")
    else:
        await message.reply(f"Sizning ma'lumotlaringiz: {user_info}")


def get_user_info(user_id):
   
    return None

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/description')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/photo2')
b4 = KeyboardButton('/photo')
kb.add(b1).add(b2).insert(b3).insert(b4)

HELP_COMMAND = """
<b>/start</b> - <em>старт бота</em>
<b>/help</b> - <em>список команд</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка фото</em>
<b>/photo2</b> - <em>отправка фото2</em>"""


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Бобро Поржаловать в этот кривой бот",
                           parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Этот бот умеет отправлять фото",
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo="https://i.pinimg.com/originals/1a/11/ac/1a11acb77be5eaed4893f46b36aec3dd.jpg")
    await message.delete()

@dp.message_handler(commands=['photo2'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo="https://avatars.mds.yandex.net/i?id=7fbdc9a0f64a12a8eec18b2226781ec368ab382a-7552332-images-thumbs&n=13")
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb
import bot_messages

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.reply(bot_messages.start_message, reply_markup=kb.start_kb)

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.reply(bot_messages.help_message)

@dp.message_handler(commands=['quote_by_topic'])
@dp.message_handler(regexp='Цитаты по теме')
async def send_quotes_by_topic(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отправил цитату по теме')

if __name__ == '__main__':
    executor.start_polling(dp)
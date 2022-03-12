from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import keyboards as kb
import messages as msgs

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.reply(msgs.start_message, reply_markup=kb.start_kb)

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.reply(msgs.help_message)

@dp.message_handler(commands=['quote_by_topic'])
@dp.message_handler(regexp='📚Цитаты по теме')
async def get_topic(message: types.Message):
    await dp.current_state(user=message.from_user.id).set_state('get_topic')
    await bot.send_message(message.from_user.id, msgs.choose_topic_message,
                           reply_markup=kb.cancel_kb)

@dp.message_handler(state='get_topic')
async def send_quotes_by_topic(message: types.Message):
    #await dp.current_state(user=message.from_user.id).reset_state()
    await bot.send_message(message.from_user.id, r'"Отправил тебе цитаты по теме"',
                           reply_markup=kb.start_kb)



    

if __name__ == '__main__':
    executor.start_polling(dp)
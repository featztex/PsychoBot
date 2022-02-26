from config import API_TOKEN
from calls_from_storage import take_random_quote
from aiogram import Bot, Dispatcher, executor, types

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

buttons_text = ['Рандомная цитата', 'Викторина']

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start`
    """
    keyboard_markup = types.ReplyKeyboardMarkup()
    keyboard_markup.row(*buttons_text)
    await message.reply('Привет!\n Я первый тестовый бот\n', reply_markup=keyboard_markup)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/help`
    """
    await message.reply('Я могу отправить тебе рандомную цитату\n')

@dp.message_handler(regexp='Рандомная цитата')
async def send_random_quote(message: types.Message):
    """
    This handler will be called when user sends `Рандомная цитата`
    """
    await message.reply(take_random_quote() + '\n')

@dp.message_handler(regexp='Викторина')
async def make_quiz(message: types.Message):
    #need to create realisation of quiz here
    pass

@dp.message_handler(lambda message: message.text not in buttons_text)   
async def reply_to_other_messages(message: types.Message):
    await message.reply('Я пока не умею отвечать на другие запросы\n')

if __name__ == '__main__':
    executor.start_polling(dp)

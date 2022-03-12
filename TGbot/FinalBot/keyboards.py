#Модуль для работы с клавиатурами

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

start_kb_buttons = ['📚Цитаты по теме', '🎲Викторина']
start_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*start_kb_buttons)
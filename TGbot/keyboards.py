#Модуль для работы с клавиатурами

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from random import randint, shuffle
import pandas as pd
import os.path as op
from bot import DATA_PATH


AUTHORS_FOR_QUIZ = pd.read_csv(op.join(DATA_PATH, 'authors_for_quiz.csv')).values.tolist()

start_kb_buttons = ['📚Цитаты по теме', '🎲Викторина']
start_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*start_kb_buttons)

clear_kb = ReplyKeyboardRemove()

cancel_kb = ReplyKeyboardMarkup(resize_keyboard=True).add('🔙 Назад')

quizzes = ['Угадай автора по цитате']
choose_quiz_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(*quizzes)
choose_quiz_kb.add('🔙 Назад')

def guess_author_kb(correct_author, quiz_id):
    wrong_authors = set()
    while len(wrong_authors) < 3:
        wrong_authors.add(AUTHORS_FOR_QUIZ[randint(0, len(AUTHORS_FOR_QUIZ) - 1)][1])
    authors_and_answers = [(correct_author, 'correct')] +\
                         [(wrong_author, 'wrong') for wrong_author in wrong_authors]
    shuffle(authors_and_answers)

    authors_bttns = (InlineKeyboardButton(author, callback_data=answer+' '+str(quiz_id)) for
                    author, answer in authors_and_answers)
    authors_kb = InlineKeyboardMarkup(row_width=3)
    for button in authors_bttns:
        authors_kb.add(button)
    return authors_kb

# Описание

В этой папке представлены все датасеты, которые так или иначе пригодились в нашем проекте, а также скрипты, с помощью которых они создавались

# data

## Файлы для использования:

- big_data.csv — обработанные данные <цитата—автор—теги> с парой добавленных фичей с https://mislitel.info/ (35к строк), наш основной датасет без энкодинга (переехал в TGBot)

- data_for_quiz_1.csv — небольшой датасет <цитата—автор> для викторины (120 строк) (переехал в TGBot)

- processed_data.csv — big_data.csv с энкодингом по всем хештегам, удалены бесполезные столбцы (теги, по которым находится меньше 10 фраз)

- cleaned_tagged.txt — очищенный текстовик с цитатами (12к строк)

- data.csv — чистые данные <цитата—автор> с http://uaforizm.com/ (1к строк)


## Служебные файлы:

- authors_for_quiz.csv — уникальные авторы из data_for_quiz_1.csv (переехал в TGBot)

- links.csv — ссылки на разделы http://uaforizm.com/

- links2.csv — ссылки на топ 500 авторов https://mislitel.info/

- tags.csv — уникальные теги big_data.csv


## other

- conversation1.txt — 330к строк с тренировочными диалогами

- conversation2.txt — 200к строк с диалогами из книг

- poetry.csv — 17к небольших стихотворений

- questions.txt — 60к вопросительных предложений

- short.txt — 320к коротких предложений и словосочетаний


# scripts 

- df_concat.py — небольшой скрипт для сборки big_data.csv

- encoding_for_big_data.py — энкодинг по тегам для big_data.csv

- processing_big_data.py — косметическая обработка и добавление пары новых фичей в big_data.csv

- parser_links.py — скрипт создания links.csv (c uaforizm.com)

- parser_links2.py — скрипт создания links2.csv (c mislitel.info)

- parser_phrases.py — парсим uaforizm.com, создаем data.csv

- parser_phrases2.py — парсим mislitel.info, создаем big_data.csv

- parser_tags.py — скрипт создания tags.csv

- processing_tagged.py — чистим tagged.txt, он превращается в cleaned_tagged.txt

- quiz_1.py — данные для викторины

- quiz_2.py — скрипт создания authors_for_quiz.csv
# Класс Quote
При инициализации нужно указать основные пути до данных(path_to_data, path_to_csv) и до модели (path_to_model)
Метод preprocess_text получает на вход текст и выдает "обработанный" текст, который используется в подборе цитат. Обработка это лемматизация и удаление "stopwords"
Основной метод класса basic_model использует обработанный текст и выдает list из предлагаемых циатат

# Консольное приложение
В console.py представлена консольная версия для отладки и проверки работы. 

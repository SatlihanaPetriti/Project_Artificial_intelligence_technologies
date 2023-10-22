from bs4 import BeautifulSoup
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Загрузка стоп-слов
nltk.download('stopwords')
# Чтение содержимого из файла output.html
with open("output.html", "r", encoding="utf-8") as input_file:
    content = input_file.read()
# Определение ключевых слов
keywords = ["Ученые", "врач", "алкоголик", "Россия", "здоровье", "медицина"]
# Получение списка стоп-слов
stop_words = set(stopwords.words('russian'))
# Разбор HTML-контента с помощью BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
# Находим все текстовое содержимое
text = soup.get_text()
# Токенизация текста на слова и преобразование их в нижний регистр
words = re.findall(r'\b\w+\b', text.lower())
# Фильтрация ключевых слов и стоп-слов
filtered_words = [word for word in words if word in keywords or word not in stop_words and not word.isdigit()]
# Анализ частоты встречаемости слов
word_count = Counter(filtered_words)
## Получение наиболее часто встречающихся слов
words_frequency = word_count.most_common()
# Вывод и сохранение наиболее часто встречающихся слов в файл
with open("words_frequency.txt", "w", encoding="utf-8") as output_file:
    for word, count in words_frequency:
        output_file.write(f"{word}: {count}\n")
        print(f"{word}: {count}")
print("Самые часто встречающиеся слова сохранены в 'words_frequency.txt'.")

from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Загрузка стоп-слов
nltk.download('stopwords')
# Чтение содержимого из файла output.html
with open("output.html", "r", encoding="utf-8") as input_file:
    content = input_file.read()
# Разбор HTML-контента с помощью BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')
# Находим всё текстовое содержимое
text = soup.get_text()
# Токенизация текста на предложения
sentences = re.split(r'(?<=[.!?])\s', text)
# Определение функции для фильтрации и очистки текста
def text_filter(text):
    text = text.lower() # Преобразование текста в нижний регистр
    words = re.findall(r'\b\w+\b', text) # Разделение текста на слова
   # Удаление стоп-слов и чисел
    stop_words = set(stopwords.words('russian'))
    words = [word for word in words if word not in stop_words and not word.isdigit()]
    return " ".join(words)
# Фильтрация и очистка каждого предложения
cleaned_sentences = [text_filter(sentence) for sentence in sentences]
# Создание TF-IDF
tf_idf = TfidfVectorizer()
# Обучение и преобразование предложений в признаки TF-IDF
tf_idf_matrix = tf_idf.fit_transform(cleaned_sentences)
# Получение имен признаков (слов) из векторизатора
feature_names = tf_idf.get_feature_names_out()
# Перебор предложений и их индексов
for i, sentence in enumerate(sentences):
     # Получение TF-IDF значения для текущего предложения
    tf_idf_sentence = tf_idf_matrix[i]
     # Сортировка индексов по возрастанию
    sort_index = tf_idf_sentence.indices.argsort()
     # Перебор отсортированных индексов
    for idx in sort_index:
        # Получение слова по индексу
        word = feature_names[idx]
         # Получение значения TF-IDF для слова
        tfidf_value = tf_idf_sentence.data[idx]
        # Вывод слова и его TF-IDF значения с округлением до 4 знаков после запятой
        print(f"{word}: {tfidf_value:.4f}")
    print()

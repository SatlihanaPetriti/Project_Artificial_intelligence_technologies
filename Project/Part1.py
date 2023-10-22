import requests
from bs4 import BeautifulSoup
import re
import html

# Определение списка URL-адресов
# https://medvestnik.ru/content/roubric/medicine Не открывается. Открывается только с VPN
urls = [
    "https://medportal.ru/mednovosti/",
    "https://minobrnauki.gov.ru/press-center/",
    "https://rscf.ru/news/"
]
# Определение ключевых слов
keywords = ["ученые", "врач", "алкоголик", "Россия", "здоровье", "медицина"]
# Инициализация списка для хранения текстового содержимого с URL-адресов
documents = []
# Создание функции для извлечения соответствующих предложений и их добавления в список documents
def extract_sentences(url, keywords):
    # Отправка HTTP-запроса GET на URL-адрес
    response = requests.get(url)
    # Проверка успешности запроса
    if response.status_code == 200:
        # Разбор HTML-контента с помощью BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Находим всё текстовое содержимое
        text = soup.get_text()
        # Используем регулярные выражения для разделения текста на предложения
        sentences = re.split(r'(?<=[.!?])\s', text)
        # Фильтрация и добавление предложений, содержащих хотя бы одно из ключевых слов, в список documents
        filter_sentences = [sentence for sentence in sentences if any(keyword in sentence for keyword in keywords)]
        documents.extend(filter_sentences)
    else:
        print(f"Не удалось получить {url}. Код состояния: {response.status_code}")
# Перебор списка URL-адресов и извлечение соответствующих предложений
for url in urls:
    extract_sentences(url, keywords)
# Создание одной HTML-страницы для сохранения содержимого
with open("output.html", "w", encoding="utf-8") as output_file:
    # Запись соответствующих предложений в выходной файл в виде абзацев
    for sentence in documents:
        output_file.write(f"<p>{html.unescape(sentence)}</p>")
import matplotlib.pyplot as plt

# Чтение данных из файла
with open("words_frequency.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
# Разбор слов и их частот
word_frequency = {}
for line in lines:
    word, frequency = line.strip().split(": ")
    word_frequency[word] = int(frequency)
# Сортировка слов по частоте в убывающем порядке
sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
# Взятие верхних 50 слов и их (30)частот
top_words = list(sorted_word_frequency.keys())[:50]
top_frequencies = [sorted_word_frequency[word] for word in top_words]
# Создание столбчатой диаграммы
plt.figure(figsize=(12, 8))
plt.barh(top_words, top_frequencies, color='blue')
plt.xlabel('Частота')
plt.title('Топ 30 слов по частоте')
plt.gca().invert_yaxis() # Инвертировать порядок для наиболее частых слов наверху
#График
plt.tight_layout()
plt.show()

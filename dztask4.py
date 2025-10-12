with open('PYTHON-LICENSE.txt',encoding='utf-8') as file:
    text = file.read()

word_count = {}

for char in '.,!?;:"()[]{}':
    text = text.replace(char, ' ')

words = text.lower().split()

for word in words:
    if word:
        word_count[word] = word_count.get(word, 0) + 1

top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

print("10 самых частых слов:")
for i, (word, count) in enumerate(top_words, 1):
    print(f"{i}. '{word}': {count} раз")
def count_words(text):
    return len(text.split())
def count_chars(text):
    return len(text.replace(" ", ""))
word = input("Введите фразу: ")
print(f"Сколько слов: {count_words(word)}")
print(f"Сколько слов (без пробела): {count_chars(word)}")
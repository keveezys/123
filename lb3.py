vowels = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е", "a", "e", "i","o","u","y"]
words = input("Введите слова: ").split()
for word in words:
    if word[0].lower() in vowels:
        print(word)
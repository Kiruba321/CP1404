text = input("Text: ")

word_to_count = {}
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(word_to_count.keys())
words.sort()

max_length = max(len(word) for word in word_to_count.keys())
for word in sorted(word_to_count.keys()):
    print(f"{word:{max_length}} : {word_to_count[word]}")

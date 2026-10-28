text = input("Enter text: ").lower()
word_freq = {}

for word in text.split():
    word_freq[word] = word_freq.get(word, 0) + 1

for word, freq in word_freq.items():
    print(f"Most frequent word: {word} ({freq})")
data = open('/Users/Simon/Desktop/Coding/python/code3/romeo-full.txt')

counts = {}

for line in data:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

word_count = None
selected_word = None

for word, count in counts.items():
    if word_count is None or word_count < count:
        word_count = count
        selected_word = word

print(selected_word, word_count)
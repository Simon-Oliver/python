

sentence = open('/Users/Simon/Desktop/Coding/python/code3/romeo-full.txt').read()
dict = {}
sentence= sentence.lower()
words = sentence.split()

for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

print(dict)
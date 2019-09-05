emoji_mapping = {
    ':)': '🙂',
    ':(': '🙁'
}

message = input('>>> ')
words = message.split(' ')

output = ''
for word in words:
    output += emoji_mapping.get(word, word) + ' '

print(output)

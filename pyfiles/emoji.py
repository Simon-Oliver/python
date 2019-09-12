message = input('>>> ')


def emoiji_converter(message):
    words = message.split(' ')
    emoji_mapping = {
        ':)': '🙂',
        ':(': '🙁'
    }

    output = ''
    for word in words:
        output += emoji_mapping.get(word, word) + ' '

    return output


print(emoiji_converter(message))

import re

obj = [
    {
        "name": 'Max',
        "employer": 'Disneyland',
        "email": 'max@test.com',
        "age": "25"
    },
    {
        "name": 'Oli',
        "employer": 'Apple',
        "email": 'oli@test.com',
        "age": "50"
    },
    {
        "name": 'James',
        "employer": 'Microsoft',
        "email": 'james@test.com',
        "age": "23"
    },
    {
        "name": 'Sarah',
        "employer": 'Target',
        "email": 'sarah@test.com',
        "age": "46"
    }
]


msg = '''
Hi {name},
You are {age} old.
This is a test message.
This was sent to {email} from {employer}.
'''


def replace(message, placeholders):
    msg = message
    data = re.findall('{(\w*)}', message)
    for item in data:
        string = '{' + item + '}'
        msg = msg.replace(string, placeholders[item])

    return msg.strip()


for person in obj:
    print(replace(msg, person))

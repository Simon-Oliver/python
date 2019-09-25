import re

obj = [
{
    "name": 'Max',
    "employer": 'Disneyland',
    "email": 'max@test.com'
},
{
    "name": 'Oli',
    "employer": 'Apple',
    "email": 'oli@test.com'
},
{
    "name": 'James',
    "employer": 'Microsoft',
    "email": 'james@test.com'
},
{
    "name": 'Sarah',
    "employer": 'Target',
    "email": 'sarah@test.com'
}
]


msg = '''
Hi {name},
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


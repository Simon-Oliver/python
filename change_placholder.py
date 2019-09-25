import re

obj = {
    "name": 'Max',
    "employer": 'Disneyland',
    "email": 'max@test.com'
}


message = '''
Hi {name},
This is a test message.
This was sent to {email} from the company {employer}.
'''

msg = ''

data = re.findall('{(\w*)}', message)

for item in data:
    string = '{' + item + '}'
    message = message.replace(string, obj[item])

print(message)


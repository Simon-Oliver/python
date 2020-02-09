import requests

myobj = {'somekey': 'somevalue'}

x = requests.post('http://localhost:8000/api/world', data={"post": "test1234"})

print(x)
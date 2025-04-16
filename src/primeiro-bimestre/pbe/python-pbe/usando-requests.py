import requests

req = requests.get('https://api.github.com/events')
print(req.json())







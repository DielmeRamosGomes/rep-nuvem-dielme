import requests
# pip install requests

nome_cidade = input('Nome da cidade Ex Sao_Paulo: ')

req = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude=-23.5475&longitude=-46.6361&hourly=temperature_2m&timezone=America%2F{nome_cidade}&forecast_days=1')
print(req.status_code)
# print(req.json())
print(req.json(['temperature_2m'][0]))

# acessar https://awesomeapi.com.br para criar a chave de cambio
# pip install requests
import requests
import json

CHAVE_API = 'b2e1f39d5787d64b71d7ce3b3782275143206b3fa7d392b7ab54022c4302d1db'
URL = f'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL?token={CHAVE_API}'

resposta = requests.get(URL)

if resposta.status_code == 200:
    try:
        cotacoes = resposta.json()
        print("Cotações obtidas com sucesso:")
        
        # Uso do json.dumps para imprimir o resultado de forma formatada e legível.
        #print(json.dumps(cotacoes, indent=4))
        print(f"1 Dólar = R$ {cotacoes['USDBRL']['high']}")
        print(f"Horario da cotação: {cotacoes['USDBRL']['create_date']}")
        print(f"1 Euro = R$ {cotacoes['EURBRL']['high']}")
        print(f"Horario da cotação: {cotacoes['EURBRL']['create_date']}")
    except requests.exceptions.JSONDecodeError:
        print("Erro: A resposta não está em um formato JSON válido.")
        print("Conteúdo da resposta:", resposta.text)
else:
    print(f'Erro ao obter as cotações. Código de status: {resposta.status_code}')

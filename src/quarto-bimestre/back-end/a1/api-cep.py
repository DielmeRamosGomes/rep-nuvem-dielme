import requests
import json

CHAVE_API = 'b2e1f39d5787d64b71d7ce3b3782275143206b3fa7d392b7ab54022c4302d1db'
CEP = '03694-060'
URL = 'https://cep.awesomeapi.com.br/json/'+f'{CEP}'+'?token='+f'{CHAVE_API}'

resposta = requests.get(URL)
if resposta.status_code == 200:
    try:
        dados = resposta.json()
        print("CEP obtido com sucesso!")
        #print(json.dumps(dados, indent=4))
        print(f"Nome da Rua: {dados['address_name']}")
        print(f"Distrito: {dados['district']}")
        print(f"Cidade: {dados['city']}")
        print(f"Estado: {dados['state']}")
    except requests.exceptions.JSONDecodeError:
        print("Erro: A resposta não está em um formato JSON válido.")
        print("Conteúdo da resposta:", resposta.text)
else:
    print(f'Erro ao obter o CEP. Código de status: {resposta.status_code}')


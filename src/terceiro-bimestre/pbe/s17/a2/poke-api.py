# pip install requests
import requests

url_base = "https://pokeapi.co/api/v2/pokemon/"

nome_pokemon = input("Digite o nome do Pokémon: ").strip().lower()

url_completa = url_base + nome_pokemon

try:
    resposta = requests.get(url_completa)
    if resposta.status_code == 200:
        dados_pokemon = resposta.json()
        id = dados_pokemon['id']
        nome = dados_pokemon['name']
        altura = dados_pokemon['height'] / 10  # A API retorna em decímetros, então dividimos por 10 para metros
        peso = dados_pokemon['weight'] / 10    # A API retorna em hectogramas, então dividimos por 10 para quilos
        print(f"ID na Pokédex: {id}")
        print(f"Nome : {nome.capitalize()}")
        print(f"Altura: {altura} m")
        print(f"Peso: {peso} kg")
        for tipo_info in dados_pokemon['types']:
            tipo = tipo_info['type']['name']
            print(f"Tipo: {tipo.capitalize()}")
        for abilidade_info in dados_pokemon['abilities']:
            abilidade = abilidade_info['ability']['name']
            print(f"Habilidade: {abilidade.capitalize()}")
    else:
        print(f"Erro ao buscar o Pokémon. Código de status: {resposta.status_code}")
        print("Verifique se o nome do Pokémon está correto.")
except requests.exceptions.RequestException as e:
    print(f"Ocorreu um erro na requisição: {e}")
        
        
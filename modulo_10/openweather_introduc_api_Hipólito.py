import requests
from datetime import datetime


api_key = str(input("Digite sua api key:"))
cidade = str(input("Digite o nome da cidade ex: São Paulo, Pernambuco: "))

# Exercício 1
url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric'

try:
    
    resposta = requests.get(url)
    resposta.raise_for_status()  

    
    dados = resposta.json()

    
    temperatura = dados['main']['temp']
    descricao = dados['weather'][0]['description']
    umidade = dados['main']['humidity']
    vento = dados['wind']['speed']
    timestamp = dados['dt']

    
    data_hora = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    # Exercício 2
    print(f"Clima em {cidade}:")
    print(f"Data e Hora: {data_hora}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Descrição: {descricao.capitalize()}")
    print(f"Umidade: {umidade}%")
    print(f"Velocidade do Vento: {vento} m/s")

# Exercício 3
except requests.exceptions.RequestException as e:
    print(f"Erro ao conectar com a API: {e}")
except KeyError as e:
    print(f"Erro ao processar os dados: chave {e} não encontrada")

import requests


api_key = '4e02b71f67f134e7ad2e5d07012a1d38'

def buscar_filmes(titulo):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={titulo}&language=pt-BR'

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  
        dados = resposta.json()
        
        if dados['results']:
            print(f"\nEncontrados {len(dados['results'])} filme(s) para '{titulo}':\n")

            for i, filme in enumerate(dados['results'][:10], 1):
                titulo_filme = filme.get('title', 'Título não disponível')
                ano = filme.get('release_date', '')[:4] if filme.get('release_date') else 'Ano não disponível'
                sinopse = filme.get('overview', 'Sinopse não disponível')
                if len(sinopse) > 1000:
                    sinopse = sinopse[:1000] + '...'

                print(f"{i}. {titulo_filme} ({ano})")
                print(f"   Sinopse: {sinopse}")
                print()
        else:
            print(f"Nenhum filme encontrado para '{titulo}'.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
    except KeyError as e:
        print(f"Erro ao processar os dados: chave {e} não encontrada")

if __name__ == "__main__":
    print("Buscador de Filmes - TMDB API")
    print("=" * 30)

    while True:
        titulo = input("Digite o título do filme (ou 'sair' para encerrar): ").strip()

        if titulo.lower() == 'sair':
            print("Até logo!")
            break

        if titulo:
            buscar_filmes(titulo)
        else:
            print("Por favor, digite um título válido.")

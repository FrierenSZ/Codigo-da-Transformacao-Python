import json
import os

# Caminho do arquivo para armazenar contatos
ARQUIVO_CONTATOS = 'modulo_04/contatos.txt'

# Função para carregar contatos do arquivo
def carregar_contatos():
    if os.path.exists(ARQUIVO_CONTATOS):
        with open(ARQUIVO_CONTATOS, 'r') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return {}
    return {}

# Função para salvar contatos no arquivo
def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, 'w') as arquivo:
        json.dump(contatos, arquivo, indent=4)

# Função para adicionar contato
def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ").strip()
    if nome in contatos:
        print("Contato já existe. Use a opção de atualizar se necessário.")
        return
    telefone = input("Digite o telefone: ").strip()
    contatos[nome] = telefone
    print(f"Contato '{nome}' adicionado com sucesso!")

# Função para remover contato
def remover_contato(contatos):
    nome = input("Digite o nome do contato a remover: ").strip()
    if nome in contatos:
        del contatos[nome]
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print("Contato não encontrado.")

# Função para buscar contato
def buscar_contato(contatos):
    nome = input("Digite o nome do contato a buscar: ").strip()
    if nome in contatos:
        print(f"Nome: {nome}, Telefone: {contatos[nome]}")
    else:
        print("Contato não encontrado.")

# Função para listar todos os contatos
def listar_contatos(contatos):
    if contatos:
        print("\nLista de Contatos:")
        for nome, telefone in contatos.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("Nenhum contato armazenado.")

# Função principal do menu
def menu():
    contatos = carregar_contatos()
    while True:
        print("\n--- Agenda de Contatos ---")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Listar Todos os Contatos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            remover_contato(contatos)
        elif opcao == '3':
            buscar_contato(contatos)
        elif opcao == '4':
            listar_contatos(contatos)
        elif opcao == '5':
            salvar_contatos(contatos)
            print("Contatos salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

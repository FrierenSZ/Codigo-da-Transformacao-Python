import json
import os

# Função para carregar alunos existentes do arquivo
def carregar_alunos():
    arquivo_path = 'modulo_04/aluno_info.txt'
    if os.path.exists(arquivo_path):
        with open(arquivo_path, 'r') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return []

# Função para salvar alunos no arquivo
def salvar_alunos(alunos):
    arquivo_path = 'modulo_04/aluno_info.txt'
    with open(arquivo_path, 'w') as arquivo:
        json.dump(alunos, arquivo, indent=4)

# Carregar alunos existentes
alunos = carregar_alunos()

# Solicitar informações do novo aluno
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
notas_str = input("Digite as notas separadas por vírgula (ex: 8.5,9.0,7.5): ")
notas = [float(nota.strip()) for nota in notas_str.split(',')]

# Criar dicionário para o novo aluno
novo_aluno = {
    'nome': nome,
    'idade': idade,
    'notas': notas
}

# Adicionar o novo aluno à lista
alunos.append(novo_aluno)

# Salvar a lista atualizada no arquivo
salvar_alunos(alunos)

# Exibir todos os alunos armazenados
print("\nInformações de todos os Alunos armazenados:")
for i, aluno in enumerate(alunos, start=1):
    print(f"\nAluno {i}:")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")

'''

'''


class ValidarIdade(Exception):
    pass



def VerificarConta(nome , idade, genero):
    if (idade <= 0 or idade > 100):
        raise ValidarIdade(f"Digite uma idade válida {idade} não paréce ser verdade")
    else:
        print(f"Conta Criada com sucesso\n\n\nConta: {nome} \nIdade: {idade} \nGênero: {genero}")




try:
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite seu idade: "))
    genero = str(input("Digite seu genero: "))
    VerificarConta(nome, idade, genero)
except ValidarIdade as error:
    print(f"Erro {error}")


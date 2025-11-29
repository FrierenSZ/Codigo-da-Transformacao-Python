'''
pip install faker
py -m pip install faker
'''



from faker import Faker 
from datetime import datetime


fake = Faker('pt_BR')  


def calcular_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade



usuarios = []
for _ in range(5):
    nome = fake.name()
    email = fake.email()
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=80)
    idade = calcular_idade(data_nascimento)
    usuario = {
        'nome': nome,
        'idade': idade,'email': email,
        'data_nascimento': data_nascimento.strftime('%d/%m/%Y'),
        
    }
    usuarios.append(usuario)


print("Usuários fictícios gerados:")
for usuario in usuarios:
    print(f"Nome: {usuario['nome']}")
    print(f"Email: {usuario['email']}")
    print(f"Data de Nascimento: {usuario['data_nascimento']}")
    print(f"Idade: {usuario['idade']} anos")
    print("-" * 40)

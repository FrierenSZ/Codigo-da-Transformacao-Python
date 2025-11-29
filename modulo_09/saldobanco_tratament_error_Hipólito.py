"""


"""





class SaldoInsuficienteError(Exception):
    pass

def Sacar(saldo, saque):
    if saque > saldo:
        raise SaldoInsuficienteError(f"Você não tem saldo o suficiente! você tem R$ {saldo} na sua conta" )
    return saldo - saque

try:
    saldo = float(input("Digite seu saldo R$: "))
    saque = float(input("Quando você deseja sacar: R$"))
    SacarSaldo = Sacar(saldo, saque)
except SaldoInsuficienteError as error:
    print(f"Erro: {error}")
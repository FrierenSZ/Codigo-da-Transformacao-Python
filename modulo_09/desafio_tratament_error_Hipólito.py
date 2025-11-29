"""
len(senha) < 5: Verifica o comprimento mínimo.
any(c.isdigit() for c in senha): Verifica se há pelo menos um dígito (número).
any(c in simbolos for c in senha):
 Verifica se há pelo menos um símbolo usando o operador in para comparar cada caractere com a string de símbolos.

"""

import string

def validar_senha(senha):
    if len(senha) < 5:
        return False, "A senha deve ter pelo menos 5 caracteres."
    
    tem_numero = any(c.isdigit() for c in senha)
    simbolos = string.punctuation  # Inclui !@#$%^&*() etc.
    tem_simbolo = any(c in simbolos for c in senha)
    
    if not tem_numero:
        return False, "A senha deve conter pelo menos um número."
    if not tem_simbolo:
        return False, "A senha deve conter pelo menos um símbolo."
    
    return True, "Senha válida."


senha = input("Digite a senha: ")
valida, mensagem = validar_senha(senha)
print(mensagem)
"""
Lógica E (AND)
é a lógica do login
email e a senha sejam True
""""

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

"""
Lógica OU (OR)
SOL NO DOM              JOGO BR           CHURRAS NO DOM
False                   True              True
"""

logica-ou = False or False or False
print(logica_ou)

# NOT

negacao = not True
print(negacao)

if not verifica_senha:
    print("Senha invalida")
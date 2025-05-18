import os
from cadastro_contas import *
cont = 1
valor = False
def validar_senha(senha_digitada, user_digitado, contas_existentes):
    global valor, cont
    if user_digitado in contas_existentes['user']:
        loc = contas_existentes['user'].index(user_digitado)
        if contas_existentes['senha'][loc] == senha_digitada:
            valor = True
            os.system('cls')
            return valor
        else:
            os.system('cls') 
            print('Senha errada!')
            cont += 1
    else:
        os.system('cls')
        print('Usuario não existe!')
def validar_login():
    global valor, cont
    while valor == False:
        print('='*20,'VALIDANDO LOGIN','='*20)
        user = str(input('Informe o nome do usuario: '))
        senha = str(input('Informe a senha: '))
        print('----------------------------------------------------------')
        if cont < 3:
            validar_senha(senha, user, contas_existentes)
        else:
            print('Acesso negado excesso de tentativas!')
            break
    if valor == True:
        return True
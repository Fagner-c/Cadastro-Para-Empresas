#Inicio
from time import sleep
from validador_login import *
from cadastro_contas import *
while True:
    sleep(0.3)
    os.system('cls')
    print('='*20,'INICIO','='*20)
    print('[1]Cadastrar novo usuario \n[2]Entrar na conta \n[3]Sair')  
    opcao = int(input('escolha uma opção: '))
    match opcao:
        case 1:
            os.system('cls')
            print('='*20,'AREA DE ADMINISTRÇÃO','='*20)
            senha_admin = str(input('Informe a senha de adiminstrador: '))
            if senha_admin  ==  '@Adimin123':
                cadastro()
                os.system('cls')
            else:
                os.system('cls')
                print('Senha errada!')
        case 2:
            sleep(0.3)
            print('='*20,'VALIDADOR DE LOGIN','='*20)    
            validar_login()
            if validar_login() == True:
                print('='*20,'CADASTRO DE RELATORIOS','='*20)  
                menssagens = []
                while True:
                    os.system('cls')
                    if len(menssagens) > 0:
                        for t in menssagens:
                            print(f'{t['nome']}: {t['texto']}')
                        print('________________________________________________________________')
                    nome= str(input('iNFORME O NOME: '))
                    texto = str(input('Digite a menssagem: '))
                    if texto == 'fim':
                        break
                    menssagens.append({'nome' : nome, 'texto' : texto})
        case 3:
            break
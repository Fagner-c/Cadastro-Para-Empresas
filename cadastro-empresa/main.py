from time import sleep
from validador_login import *
from cadastro_contas import *
menssagens = []
if validar_login() == True:
    while True:
        try:
            sleep(0.3)
            os.system('cls')
            print('='*20,'INICIO','='*20)
            print('[1]Cadastrar novo usuario \n[2]Cadastrar relatorios \n[3]Ver relatorios \n[4]Sair')  
            opcao1 = int(input('escolha uma opção: '))
        except:
            os.system('cls')
            print('Opção invalida!')
            sleep(1)
        else:
            match opcao1:
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
                    if validar_login() == True:
                        print('='*20,'CADASTRO DE RELATORIOS','='*20)  
                        while True:
                            opcao2 = str(input('Cadastrar novo relatio [s/n]: ')).lower()
                            if opcao2 == ('s' or 'sim'):
                                    os.system('cls')
                                    nome= str(input('iNFORME O NOME: '))
                                    texto = str(input('Digite a menssagem: '))
                                    menssagens.append({'nome' : nome, 'texto' : texto})
                            else:
                                break
                case 3:
                    while True:
                        os.system('cls')
                        print('='*20,'EXIBIÇÃO DE RELATORIOS','='*20)
                        if len(menssagens) > 0:
                            for t in menssagens:
                                print(f'{t['nome']}: {t['texto']}')
                            print('________________________________________________________________')
                            sleep(3)
                            opcao3= str(input('Sair dos relatorios [s/n]: ')).lower()
                            if opcao3 == ('s' or'sim'):
                                break
                        else:
                            print('0 menssagens cadastradas!')
                            opcao3= str(input('Sair dos relatorios [s/n]: ')).lower()
                            if opcao3 == ('s' or'sim'):
                                break
                case 4:
                    break
        
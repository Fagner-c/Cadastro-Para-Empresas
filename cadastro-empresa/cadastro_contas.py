contas_existentes = {"user" : ['Fagner', 'Gustavo'], "senha": ['abacate', 'cid']}
def cadastro():
    print('='*20,'CADASTRO DE USER','='*20)
    newuser = str(input('Informe o nome do novo usuario: '))
    if newuser not in contas_existentes['user']:
        newsenha = str(input('Informe a senh do novo usuario: '))
        contas_existentes['user'].append(newuser)
        contas_existentes['senha'].append(newsenha)
        print('Novo usuario dicionado!')
    else: 
        print('Esse nome de usuario já é usado!')
    del newuser
    del newsenha  
import os
os.system('cls')

users = []
opcao = 0

print('Bem-Vindo ao Cadastro de usuários:')

def addUser():
    print('\n --- Cadastro de Novo Usuário --- ')
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    telefone = input('Digite seu telefone: ')

    new_user = [nome, email, telefone]
    users.append(new_user)
    print(f'Usuário {nome} cadastrado com sucesso!')

def showUsers():
    print('------ Usuários ------')
    if not users:
        print('Nenhum usuário cadastrado!')
        print('------------------------')
        return
    
    userNumber = 1
    for user in users:
        nome = user[0]
        email = user[1]
        telefone = user[2]
        print(f'{userNumber}. Nome: {nome}, Email: {email}, Telefone: {telefone}')
        userNumber = userNumber + 1
    print('----------------------')

def deleteUsers():
    showUsers()

    if not users:
        return
    try:
        num = int(input('Digite o número do usuário que quer remover: '))
        index = num - 1
        deletedUsers = users.pop(index)
        print(f'\nO usuário {deletedUsers[0]} foi removido com sucesso.')
    except:
        print('Erro! Número inválido ou usuário não existe.')
        
while opcao != '4':
    print('Selecione a opção desejada: \n 1. Cadastrar Usuário \n 2. Mostrar usuários cadastrados \n 3. Deletar usuário cadastrado \n 4. Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        addUser()
    elif opcao == '2':
        showUsers()
    elif opcao == '3':
        deleteUsers()
    elif opcao == '4':
        print('Saindo do sistema...')
    else:
        print('Opção Inválida! Tente novamente.')

    input('\nPressione Enter para continuar...')
    
    os.system('cls')
            

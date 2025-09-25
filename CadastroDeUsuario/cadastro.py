import os
os.system('cls')

users =[]

opcao = 0

print('Bem-Vindo ao Cadastro de usuários:')

def addUser():
    newUser = input('Digite seu nome: ')
    users.append(newUser)

def addEmail():
    newEmail = input('Digite seu e-mail: ')
    users.append(newEmail)

def addTel():
    newTelephone = input('Digite seu telefone: ')
    users.append(newTelephone)

def showUsers():
    print('------ Usuários ------')
    userNumber = 1
    for user in users:
        print(f'{userNumber}. {user}')
        userNumber = userNumber + 1
        print('-----------------------')

def deleteUsers():
    showUsers()

    if not users:
        print('Nenhum usuário cadastrado!')
        return
    try:
        num = int(input('Digite o número do usuário que quer remover: '))
        index = num - 1
        deletedUsers = users.pop(index)
        print(f'O usuário {deletedUsers} foi removido com sucesso.')
    except:
        print('Erro! Número inválido ou usuário não existe.')
        
while opcao != '4':
    print('Selecione a opção desejada: \n 1. Cadastrar Usuário \n 2. Mostrar usuários cadastrados \n 3. Deletar usuário cadastrado \n 4. Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        addUser()
    elif opcao == '2':
        addEmail()
    elif opcao == '3':
        addTel()
    elif opcao == '4':
        print('Saindo do sistema...')
    else:
        print('Opção Inválida! Tente novamente.')

    input('\nPressione Enter para continuar...')
    os.system('cls')
            

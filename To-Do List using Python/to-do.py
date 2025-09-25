import os

os.system('cls')

tasks = []
opcao = 0
print('Bem-vindo à sua lista de tarefas!')

def addTask():
    newTask = input('Adicione uma nova tarefa: ')
    tasks.append(newTask)

def showTasks():
    print("-------------- SUAS TAREFAS --------------")
    taskNumber = 1
    for tarefa in tasks:
        print(f'{taskNumber}. {tarefa}')
        taskNumber = taskNumber + 1
        print('------------------------------------------')

def deleteTask():
    showTasks()

    if not tasks:
        print('Nenhuma tarefa para deletar!')
        return 
    try:
        num = int(input('Digite o número da tarefa que quer remover: '))
        index = num - 1
        DeletedTask = tasks.pop(index)
        print(f'Tarefa {DeletedTask} foi removida com sucesso.')
    except:
        print('Erro! Número inválido ou tarefa não existe')

while opcao != '4':
    print('Digite a opção desejada:\n 1. Adicionar Tarefa \n 2. Mostrar Tarefas \n 3. Deletar Tarefas \n 4. Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        addTask()
    elif opcao == '2':
        showTasks()
    elif opcao == '3':
        deleteTask()
    elif opcao == '4':
        print('Encerrando o programa...')
    else:
        print('Opção Inválida! Tente novamente.')
        
    input('\nPressione enter para continuar')
    os.system('cls')
    
import os
os.system('cls')

print('----- Lista de Pedidos -----')

pedido = []
opcao = 0

def novo_pedido():
    print('\n--- Faça seu pedido ---')
    pratoPrincipal = input('Digite o que gostaria de comer como prato principal: ')
    bebida = input('Digite a bebida desejada: ')
    acompanhamento = input('Diga o acompanhamento desejado: ')
    sobremesa = input('Digite a sobremesa: ')

    novo_pedido = [pratoPrincipal, bebida, acompanhamento, sobremesa]
    pedido.append(novo_pedido)
    os.system('cls')
    print('\nPedido realizado com sucesso! Agora é só aguardar.')
    input('\nPressione Enter para continuar...')
    
    

def mostrar_pedido():
    print('-------- Pedidos --------')
    if not pedido:
        print('Nenhum pedido cadastrado.')
        print('----------------------')
        return
    
    numero_pedido = 1
    for i in pedido:
        pratoPrincipal = i[0]
        bebida = i[1]
        acompanhamento = i[2]
        sobremesa = i[3]
        print(f'{numero_pedido}. Prato Principal: {pratoPrincipal};\n   Bebida: {bebida};\n   Acompanhamento: {acompanhamento};\n   Sobremesa: {sobremesa}.')
        numero_pedido = numero_pedido + 1
    print('------------------------')


def deletar_pedido():
    mostrar_pedido()
    num = int(input('Selecione o número do pedido que deseja desfazer: '))
    if not pedido:
        return
    
    try:
        index = num - 1
        pedidoDeletado = pedido.pop(index)
        os.system('cls')
        print(f'\n O pedido foi deletado com sucesso!\n')
    except:
        print('Erro! Pedido ou número inválido!')

while opcao != '4':
    print('\n1. Fazer novo pedido \n2. Mostrar pedidos realizados \n3. Excluir pedido \n4. Sair\n')
    opcao = input('Selecione a opção desejada: ')
    if opcao == '1':
        os.system('cls')
        novo_pedido()
    elif opcao == '2':
        os.system('cls')
        mostrar_pedido()
    elif opcao == '3':
        os.system('cls')
        deletar_pedido()
    else:
        os.system('cls')
        print('Encerrando programa...')
        break

    
        




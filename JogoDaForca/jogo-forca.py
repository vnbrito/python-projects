import os

os.system('cls')

secretword = 'BANANA'
display = ['_', '_', '_', '_', '_', '_']

def showDisplay(display):
    print(" ".join(display)) 

for userAttempt in range(6):
    os.system('cls')
    print('Dica: É uma fruta.')
    print(f"Tentativa {userAttempt + 1} de 6")
    showDisplay(display)

    attemptletter = input('Digite uma letra: ').upper()

    # Se o jogador ACERTOU a letra...
    if attemptletter in secretword:
        print(f'\nBoa, a letra "{attemptletter}" faz parte da palavra.')
        for count in range(6):
            wordletter = secretword[count]
            if attemptletter == wordletter:
                display[count] = attemptletter

        # VERIFICA A VITÓRIA AQUI! DEPOIS DE UM ACERTO!
        if '_' not in display:
            os.system('cls')
            print('🎉 PARABÉNS! VOCÊ ACERTOU A PALAVRA! 🎉\n')
            showDisplay(display)
            print('\n')
            break # Encerra o jogo

    # Se o jogador errar a letra
    else:
        print(f'\nQue pena, a letra "{attemptletter}" não está na palavra. Você perdeu 1 vida.')

    # Pausa para poder ler a mensagem
    input('\nPressione Enter para continuar...')


print('Fim de jogo!') # Esta mensagem aparecerá no final, seja por vitória ou derrota

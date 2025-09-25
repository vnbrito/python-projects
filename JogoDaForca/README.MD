Vamos criar uma versão simples do clássico Jogo da Forca. O computador escolhe uma palavra e o jogador tenta adivinhar letra por letra.
O que o programa deve fazer:
Definir uma palavra secreta: No início do código, defina uma palavra fixa (por exemplo: "PYTHON").
Criar o "display" da palavra: Crie uma lista para mostrar o progresso do jogador. Para a palavra "PYTHON", você começaria com uma lista como ['_', '_', '_', '_', '_', '_'].
Definir um número de vidas: O jogador terá um número limitado de tentativas (por exemplo, 6 vidas).
Criar um loop principal: O jogo deve continuar enquanto o jogador tiver vidas e a palavra não tiver sido descoberta.
Pedir uma letra ao jogador: A cada rodada, peça para o jogador digitar uma letra.
Verificar a letra:
Se a letra estiver na palavra secreta: Percorra a palavra secreta. Em todas as posições onde a letra aparecer, atualize a lista de "display". Por exemplo, se a palavra for "PYTHON" e o chute for "O", o display vira ['_', '_', 'T', 'H', 'O', '_'].
Se a letra NÃO estiver na palavra secreta: O jogador perde uma vida. Informe quantas vidas restam.
Mostrar o status: A cada rodada, mostre o "display" da palavra e o número de vidas restantes.

Condições de Fim de Jogo:
Vitória: Se o jogador preencher todas as letras do "display" ('_' não estiver mais na lista), mostre uma mensagem de parabéns.
Derrota: Se as vidas chegarem a 0, informe ao jogador que ele perdeu e revele qual era a palavra secreta.

Dicas:

Use um laço while para controlar o jogo, com a condição de ter vidas e de ainda haver '_' no display.
Use um laço for para percorrer a palavra secreta e verificar se a letra chutada está nela.
Crie uma função mostrar_jogo(display, vidas) para imprimir o status atual do jogo e manter o código organizado.
Lembre-se de converter o chute do jogador para maiúsculas (ou minúsculas) para evitar problemas (chute.upper()).

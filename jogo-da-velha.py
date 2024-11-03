import os

def limpar_tela():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')

def imprimir_tabuleiro(x):
    print ( '|=== Tabuleiro ===|' )
    print ( "|-----+-----+-----|" )
    for i in range ( 3 ):
        print ( "|" + "|".join ( tabuleiro[i] ) + "|" )
        if i < 2:
            print ( "|-----+-----+-----|" )
    print ( "|-----+-----+-----|" )
    print ( '|=================|' )

def jogada_atual():
    global jogador_atual
    if verificar_vencedor():
        imprimir_tabuleiro(tabuleiro)
    while not verificar_vencedor():
        imprimir_tabuleiro(tabuleiro)
        jogada_atual = True
        while jogada_atual:
            entrada_jogador = input(f'Jogador atual: {jogador_atual}. \nDeseja ocupar qual espaço no tabuleiro?: ')
            
            # Verifica se entrada é válida
            if not entrada_jogador.isdigit() or int(entrada_jogador) < 1 or int(entrada_jogador) > 9:
                print("Entrada inválida. Por favor, digite um número entre 1 e 9.")
                continue
            
            jogada_feita = False
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    # Primeiro encontra a posição desejada
                    if tabuleiro[i][j].strip() == str(entrada_jogador):
                        # Verifica se está ocupada
                        if tabuleiro[i][j].strip() in lista_jogadores:
                            limpar_tela()
                            print('\nEspaço já ocupado. Selecione outro por favor.\n')
                            break
                        else:
                            # Faz a jogada
                            limpar_tela()
                            tabuleiro[i][j] = f'  {jogador_atual}  '
                            if jogador_atual == 'X':
                                jogador_atual = 'O'
                            else:
                                jogador_atual = 'X'
                            jogada_atual = False
                            jogada_feita = True
                            break
                if jogada_feita:
                    break
                
            if not jogada_feita and jogada_atual:
                print("Jogada inválida. Tente novamente.")

def verificar_vencedor():
    vencedor = False
    for i in range(len(tabuleiro)):
        if vencedor:
            break
        for j in range(len(tabuleiro[i])):
            if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] and tabuleiro[0][j].strip() in lista_jogadores:
                limpar_tela()
                print(f'\nJogo encerrado! O vencedor é {tabuleiro[0][j].strip()}.\n')
                return True
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0].strip() in lista_jogadores:
                limpar_tela()
                print(f'\nJogo encerrado! O vencedor é {tabuleiro[i][0].strip()}.\n')
                return True
            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0].strip() in lista_jogadores:
                limpar_tela()
                print(f'\nJogo encerrado! O vencedor é {tabuleiro[0][0].strip()}.\n')
                return True
            if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2].strip() in lista_jogadores:
                limpar_tela()
                print(f'\nJogo encerrado! O vencedor é {tabuleiro[0][2].strip()}.\n')
                return True

    if all(tabuleiro[i][j].strip() != ' ' and tabuleiro[i][j].strip() in lista_jogadores for i in range(len(tabuleiro)) for j in range(len(tabuleiro[i]))):
        limpar_tela()
        print('Jogo encerrado! Deu velha/EMPATE.')
        return True

    return False

# Início do código
nr_jogadas = 0
while True:
    if nr_jogadas == 0:
        resposta = input(f'Deseja iniciar o jogo? [S/N]')
    if nr_jogadas > 0:
        resposta = input(f'Deseja continuar o jogo? [S/N]')
    if resposta.upper() != 'S' and resposta.upper() != 'N':
        print("Resposta inválida! Digite um valor entre \s'S' para sim, ou \s'N' para não.")
    if resposta.upper() == 'S':
        # Tabuleiro inicial
        tabuleiro = [
                    ['  1  ', '  2  ', '  3  '],
                    ['  4  ', '  5  ', '  6  '],
                    ['  7  ', '  8  ', '  9  ']
                    ]
        
        # Lista de jogadores:
        lista_jogadores = ['X','O']
        # Definindo o jogador atual:
        jogador_atual = 'X'

        # Iniciando o jogo
        limpar_tela()
        jogada_atual()
        imprimir_tabuleiro(tabuleiro)
        # Somando o número de jogadas
        nr_jogadas += 1
    if resposta.upper() == 'N':
        if nr_jogadas == 0:
            print('\nPrograma encerrado. Até a próxima!\n')
        if nr_jogadas > 1:
            print(f'\nForam jogadas {nr_jogadas} partidas. Obrigado e espero que tenha se divertido!!!\n')
        if nr_jogadas == 1:
            print(f'\nFoi jogada {nr_jogadas} partida. Obrigado e espero que tenha se divertido!!!\n')
        break

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
        limpar_tela()
        imprimir_tabuleiro(tabuleiro)
        jogada_atual = True
        while jogada_atual:
            jogada_atual = False
            entrada_jogador = input(f'Jogador atual: {jogador_atual}. \nDeseja ocupar qual espaço no tabuleiro?: ')
            if not entrada_jogador.isdigit() or int(entrada_jogador) < 1 or int(entrada_jogador) > 9:
                print("Entrada inválida. Por favor, digite um número entre 1 e 9.")
                jogada_atual = True
                continue
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if tabuleiro[i][j].strip() == str(entrada_jogador):
                        if tabuleiro[i][j].strip() not in lista_jogadores:
                            tabuleiro[i][j] = f'  {jogador_atual}  '
                            if jogador_atual == 'X':
                                jogador_atual = 'O'
                            else:
                                jogador_atual = 'X'
                            jogada_atual = False
                        else:
                            print("Espaço já ocupado. Escolha outro.")
                            jogada_atual = True
                            break
            if not jogada_atual:
                break
            if jogada_atual:
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
        print('Jogo encerrado! Deu velha.')
        return True

    return False


# Início do código
# Tabuleiro inicial
tabuleiro = [
    ['  1  ', '  2  ', '  3  '],
    ['  4  ', '  5  ', '  6  '],
    ['  7  ', '  8  ', '  9  ']
]
# Lista de jogadores:
lista_jogadores = ['X', 'O']
# Definindo o jogador atual:
jogador_atual = 'X'
# Iniciando o jogo
jogada_atual()
imprimir_tabuleiro(tabuleiro)

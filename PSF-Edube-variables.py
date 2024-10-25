import math

resposta = True

while resposta:
    try:
        x = float(input('\nDigite um número: '))
        if math.isinf(x):
            print('Número muito grande ou muito pequeno. Tente novamente.')
            continue
        if math.isnan(x):
            print('Isso não é um número. Tente novamente.')
            continue
        else: print(f'''\nO valor informado para x é: {x}.
                    \nA expressão para calcular y é: y = 3x3 - 2x2 + 3x - 1.
                    \nO valor de y depois do cálculo é: {(3*x**3 - 2*x**2 + 3*x-1):.2f}.''')

        while True:
            validar = input('\nDeseja continuar? [S/N]:').upper()
            if validar in ['S','N']:
                resposta = (validar == 'S')
                break
            else: print('\nResposta inválida! Digite "S" para sim ou "N" para não.')
    except ValueError:
        print('\nEntrada inválida. Por favor digite um número válido.')

        


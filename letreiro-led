def print_number_led(num):
    led_dict = {
        '0': ['###', '# #', '# #', '# #', '###'],
        '1': ['  #', '  #', '  #', '  #', '  #'],
        '2': ['###', '  #', '###', '#  ', '###'],
        '3': ['###', '  #', '###', '  #', '###'],
        '4': ['# #', '# #', '###', '  #', '  #'],
        '5': ['###', '#  ', '###', '  #', '###'],
        '6': ['###', '#  ', '###', '# #', '###'],
        '7': ['###', '  #', '  #', '  #', '  #'],
        '8': ['###', '# #', '###', '# #', '###'],
        '9': ['###', '# #', '###', '  #', '###']
    }
    
    for i in range(5):
        line = ''
        for digit in str(num):
            line += led_dict[digit][i] + '  '
        print(line)


while True:

    try:

        number = int(input('Digite um número inteiro positivo: '))

        if number < 0:
            print('Número inválido! Deve ser positivo. Tente novamente.')
            continue
        elif type(number) != int:
            print('Numero inválido! Deve ser inteiro. Tente novamente.')
            continue
        else:
            break

    except ValueError:
        print('Valor inválido! Deve ser um número inteiro. Tente novamente.')
        continue

print_number_led(number)

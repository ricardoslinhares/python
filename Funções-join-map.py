def retorna_quadrado(x):
    return ', '.join(map(lambda x: f"{x**2}", x))+'.'

def retorna_join_nums(x):
    return ', '.join(map(str, x))+'.'

def retorna_par_impar(x):
    return ', '.join(map(lambda x: f'{x} é Par' if x % 2 == 0 else f'{x} é Ímpar', x))+'.'

nums = [1, 2, 3, 4, 5]
texto_1 = retorna_quadrado(nums)
texto_2 = retorna_join_nums(nums)
texto_3 = retorna_par_impar(nums)
print(texto_1)
print(texto_2)
print(texto_3)


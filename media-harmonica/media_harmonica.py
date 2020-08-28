def media_harmonica(lista):
    soma = 0
    for i in lista:
        soma += i ** -1
    media = len(lista) / soma
    return f'{media:.2f}'


cal = media_harmonica([3.6, 8.9, 10])
print(cal)

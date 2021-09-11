# Escolhendo entre 1 a 10 números de 1 a 99 de duas maneiras

'''def aleatorio():
    from random import randint
    lista = []
    for n in range(randint(1, 10)):
        lista.append(randint(0, 100))
    print(f'Foram escolhidos {len(lista)} números.' if len(lista) > 1 else 'Foi escolhido 1 número.')
    print(f'Os números escolhidos foram:\n{lista}' if len(lista) > 1 else f'O número escolhido foi:\n{lista}')'''


# forma mais prática de aplicar a sintaxe python
from random import randint, sample
lista = list(range(1, 100))
lista_aleatoria = sample(lista, randint(1, 10))
print(f'Foram escolhidos {len(lista_aleatoria)} números.' if len(lista_aleatoria) > 1 else 'Foi escolhido 1 número.')
print(f'Os números escolhidos foram:\n{lista_aleatoria}' if len(lista_aleatoria) > 1 else f'O número escolhido foi:\n{lista_aleatoria}')

def aleatorio():
    from random import randint
    lista = []
    for n in range(randint(1, 10)):
        lista.append(randint(0, 100))
    print(f'Foram escolhidos {len(lista)} números.' if len(lista) > 1 else 'Foi escolhido 1 número.')
    print(f'Os números escolhidos foram:\n{lista}' if len(lista) > 1 else f'O número escolhido foi:\n{lista}')


aleatorio()

def pegarlados():
    for i in range(1, 4):
        lista.append(eval(input(f'Digite o {i}º valor: ')))
    return max(lista)


def eh_triangulo():
    a = pegarlados()
    if a < sum(lista) - a:
        print('Os lados formam um triângulo: ')
        if lista[0] == lista[1] == lista[2]:
            print('-> Equilátero')
        elif lista[0] != lista[1] != lista[2] and lista[1] != lista[2]:
            print('-> Escaleno')
        else:
            print('-> Isóceles')
    else:
        print('Os lados não formam um triângulo')


lista = []
eh_triangulo()

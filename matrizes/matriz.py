def transposta(m):
    matriz_final = []
    for i, l in enumerate(m):
        lista = []
        for j, e in enumerate(l):
            e = m[j][i]
            lista.append(e)
        matriz_final.append(lista)
    return matriz_final

def mostrar(m):
    for i in m:
        for j in i:
            print(f'[ {j:2} ]', end=' ')
        print()

def matriz(m):
    print('\nA matriz passada foi:\n')
    mostrar(m)
    print('\nSua matriz transposta é:\n')
    transposta(m)
    mostrar(transposta(m))

matriz([[3, 5], [8, 6]])

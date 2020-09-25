def transposta(m):
    return map(lambda *row: [elem for elem in row], *m)

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

def decimal(n, b2):
    lista = []
    dec = 0
    digito = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
    for c in range(len(n)):
        lista.append(n[c])
    pot = 0
    for p, e in enumerate(lista):
        if e.isalpha():
            lista[p] = digito[e]
    for p in range(len(lista) - 1, -1, -1):
        dec += int(lista[p]) * pow(b2, pot)
        pot += 1
    print(f'O nº {n} na base {b2}, em decimal é {dec}')

def naodecimal(n, b2):
    num = n
    n2 = []
    digito = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    while n >= b2:
        n2.append(str(n % b2))
        n = n // b2
    n2.append(str(n))
    for p, e in enumerate(n2):
        if int(e) > 9:
            n2[p] = digito[e]
    print(f'Nº {num}, na Base {b2} = ', end='')
    for e in range(len(n2) - 1, -1, -1):
        print(n2[e], end='')

def fatorial_exp(n):
    fat = 1
    sub = n
    for c in range(n, 0, -1):
        print(f'{sub}', end=' x ' if sub > 1 else ' = ')
        sub -= 1
        fat *= c
    return  print(fat)


def fatorial_res(n):
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
    return print(fat)


fatorial_exp(8)
fatorial_res(10)

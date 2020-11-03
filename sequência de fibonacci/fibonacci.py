import time


def f_rec(n):
    if n < 2:
        return n
    else:
        res = f_rec(n - 1) + f_rec(n - 2)
        return res


def f_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = f_mem(n - 1) + f_mem(n - 2)
        return m[n]


def f_it(n):
    res = n
    a, b = 0, 1
    for e in range(2, n + 1):
        res = a + b
        a, b = b, res
    return res


m = {}
num = 35
start = time.time()
print(f_it(num))
print(f'Iterativa: {time.time() - start}')
start = time.time()
print(f_mem(num))
print(f'Memoização: {time.time() - start}')
start = time.time()
print(f_rec(num))
print(f'Recursiva: {time.time() - start}')

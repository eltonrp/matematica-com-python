def bhaskara():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    delta = (b**2) - 4*(a * c)
    x1 = (- b + sqrt(delta)) / (2 * a)
    x2 = (- b - sqrt(delta)) / (2 * a)
    print(f'x1 = {x1:.2f} e x2 = {x2:.2f}')


from math import sqrt
bhaskara()

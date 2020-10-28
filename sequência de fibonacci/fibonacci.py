def fibo(n):
    """
    :param n: parâmetro que indica a posição desejada
    :return: retorna o valor da posição desejada
    """
    if n == 0:  # ---> Pos 0 == 0
        return 0
    elif n == 1:  # ---> Pos 1 == 1
        return 1
    else:
        res = fibo(n - 1) + fibo(n - 2)  # ---> Uso da Recursão  
        return res

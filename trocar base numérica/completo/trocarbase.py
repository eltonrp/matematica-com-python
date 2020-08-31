def trocarbase(msg1, msg2):
    from basenum.decimal import decimal
    from basenum.naodecimal import naodecimal
    número = str(input(msg1)).upper().strip()
    escolha = int(input(msg2))
    if escolha == 1:
        base = int(input('Digite a base desejada: '))
        return naodecimal(int(número), base)
    if escolha == 0:
        base = int(input('Qual base está o número: '))
        return decimal(número, base)


n = trocarbase('Digite o nº para transformar: ',
               'Escolha a base:\n'
               '[ 0 ] PARA decimal\n'
               '[ 1 ] PARA outra base\n'
               '------------> ')

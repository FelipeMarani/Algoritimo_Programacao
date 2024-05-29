x = float(input("Digite um numero real positivo ou negativo: "))
def absoluto(x):
    if x >= 0:
        print("O valor absoluto de {} é {}".format(x, x))
        return 0
    else:
        ngt = x * -1
        print("O valor absoluto de {} é {}".format(x, ngt))
        return ngt
absoluto(x)
import math
def exp(b, ex):
    rst = pow(b , ex)
    return rst
b = int(input("Digite o valor da base: "))
ex = int(input("Digite o valor do expoente: "))
valorF = exp(b, ex)
print("{} ^ {} = {}".format(b, ex, valorF))
x = int(input("Digite um numero natural: "))
for i in range(1, x+1):
    dv = i
if x / i == 0:
        print("Não é primo {}".format(x))
elif x / 1 == 0 and x / x == 1:
        print("É um numero primo {}".format(x))
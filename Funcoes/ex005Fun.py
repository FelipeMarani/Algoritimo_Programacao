x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
def dv(x, y):
    if y <= 0:
        print(-1)
        return 0
    else: 
        print(x/y)
        return 0
dv(x, y)
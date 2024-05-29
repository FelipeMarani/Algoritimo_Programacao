x = int(input("Digite um numero inteiro qualquer: "))
def nat(x):
    if x > 0:
        return x
    else:
        return x
def fat(x):
    if x > 0:
        for i in range(x+1 , 1):
            result *= i
            print(result)
            return 0
    else:
        print("O fatorial só é definido por numeros naturais")
        return 0
fat(x) 
lis = []
while True:  
    x = int(input("Digite um número maior que zero: "))
    lis.append(x)
    if x == 0:
        break
print("O maior numero é {}".format(max(lis)))
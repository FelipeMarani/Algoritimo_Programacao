total = 0
cont = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    elif num % 3 == 0:
        total += num
        cont += 1
med = total / cont
print(round(med, 2))
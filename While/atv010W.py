while True:
    idade = int(input("Digite sua idade ou digite zero para parar o programa: "))
    if idade < 0:
        continue
    elif idade > 120:
        continue
    elif idade == 0:
        print("O programa finalizou.")
        break
    elif 0 < idade < 18:
        print("Menor de idade {}".format(idade))
    else:
        print("Maior de idade {}".format(idade))
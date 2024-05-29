nome = input("Digite Seu primeiro Nome: ").upper()
Letra = nome[0]
if Letra in 'ADSB':
    valor = float(input("Digite o valor a pagar: "))
    prc = valor - (valor * 0.3)
    print(prc, "esse é o seu desconto")
else:
    print("Que pena. Nesta semana o desconto não é para seu nome, mas continue nos prestigiando e comprando que sua vez chegará em breve")
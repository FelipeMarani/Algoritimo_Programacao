total = 0
while True:
    vlr = float(input("Digite o valor do Produto: ")).__round__(2)
    if vlr == 0 or vlr < 0:
        break
    total += vlr
print("O valor total da compra fica em R${}".format(total))
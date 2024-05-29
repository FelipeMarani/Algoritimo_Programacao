dic = {}
cont = 0
while cont < 4:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    if dic.get(nome):
        print("Produto já adicionado", nome, "Digite novamente")
        continue
    else:
        dic[nome] = preco
        cont += 1
print(dic)
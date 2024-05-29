class Carro:
    marca = str
    modelo = str
    ano = int
    preco = float
    cor = str
    estado = str

lisCAr = []
for i in range(3):
    v = Carro()
    v.marca = str(input("Digite a marca do veículo: "))
    v.modelo = str(input("Digite a modelo do veículo: "))
    v.ano = int(input("Digite a ano do veículo: "))
    v.preco = float(input("Digite a preço do veículo: "))
    v.cor = str(input("Digite a cor do veículo: "))
    v.estado = str(input("Digite a estado do veículo: "))
    lisCAr.append(v)
for i in range(3):
    print(" Marca: ",lisCAr[i].marca, " Modelo: ", lisCAr[i].modelo, " ano: ", lisCAr[i].ano, "preço: ", lisCAr[i].preco,"cor: ", lisCAr[i].cor,"estado: ", lisCAr[i].estado)
    
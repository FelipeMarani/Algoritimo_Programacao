# Exercício 1
class User:
  nome = str
  cpf = int
  senha = str
  data_Nasc = str

user1 = User()
user1.nome = "Felipe Jesus"
user1.cpf = 49348888889
user1.senha = "Fels020202020220"
user1.data_Nasc = '23/04/2005'

user2 = User()
user2.nome = "Gustavo La roche"
user2.cpf = "493488875989"
user2.senha = "Lapedrita02022@"
user2.data_Nasc = '12/02/2005'

print("Nome: ", user1.nome)
print("cpf: ", user1.cpf)
print("senha: ",user1.senha)
print("Data de Nascimento: ",user1.data_Nasc)

print("\nNome: ", user2.nome)
print("cpf: ", user2.cpf)
print("senha: ",user2.senha)
print("Data de Nascimento: ",user2.data_Nasc)
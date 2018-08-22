def menu():
  print('''enu
        2 - Dadois financeiros
        3 ''')
def soma(cred,alu,sla,luz):
  r = cred+alu+sla+luz
  return print("Você deve por mês: R$",r)
  


print("Bem vindo! Complete com os seus dados financeiros.
      \n")


cred = int(input("Cartão de crédito: R$"))
alu = int(input("Aluguel: R$"))
sla = int(input("Agua: R$"))
luz = int(input("Luz: R$"))
soma(cred,alu,sla,luz)

input("---------------PRESIONE ENTER PARA CONTINUAR------------------")












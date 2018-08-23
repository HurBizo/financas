
import os

Nome = ["Cartão","Luz","Agua","Aluguel"]
Valor = [0]

class Fina:
    def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def novoDes():
        Fina.limpar()
        Valor.pop()
        Nome.append(input("Digite o nome da despesa: "))
        Valor.append(input("Valor: R$"))
        print(nome, "-", i)
        input("\nAdicionado com sucesso! precione ENTER para continuar\n\n")
        Fina.limpar()
        Fina.menu()
    def count(a):
        return a + 1
    
    def soma():
        Valor = []
        
    def ajuste():
        Fina.limpar()
        print("Bem vindo! Digite suas informaçoes.")
        
        Valor.append(int(input("Cartão: ")))
        Valor.append(int(input("Luz: ")))
        Valor.append(int(input("Agua: ")))
        Valor.append(int(input("Aluguel: ")))
        
        r = sum(Valor)
        print("Suas despesas são de R$",r )
        input()
        
        Fina.menu()
        
    def resumo():
        Fina.limpar()
        if Valor == 0:
          print("Você ainda não preencheu seu quadro financeiro!")
          input()
          Fina.ajuste()
        print('''
 Seu resumo geral ficou
''',sum(Valor))
        
    def menu():
        Fina.limpar()
        s = int(input('''
Escolha una opção de sua prederencia:
1 - Ajuste de dados.
2 - Adicionar despesas
3 - Resumo geral
4 - Adicionar lucro
'''))
        print(Valor)
        input()
        
        if(s == 1):
          Fina.ajuste()
        elif(s == 3):
    	    Fina.resumo()
        elif(s == 2):
          Fina.novoDes()
                
        else:
          print("fim!")
       
        	
Fina.menu()


import os
class Fina:
    def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def novoDes():
        Fina.limpar()
        nome = input("Digite o nome da despesa: ")
        i = int(input("Valor: R$"))
        print(nome, "-", i)
        input("\nAdicionado com sucesso! precione ENTER para continuar\n\n")
        Fina.limpar()
        Fina.menu()
        
    def ajuste():
        print("Bem vindo! Digite suas informaçoes.")
    
        card = int(input("Cartão: "))
        luz = int(input("Luz: "))
        agua = int(input("Agua: "))
        alugue = int(input("Aluguel: "))
    
        input("Suas despesas são de R$",int(r) ," !")
    
        
    def menu():
        Fina.limpar()
        s = int(input('''
Escolha una opção de sua prederencia:
1 - Ajuste de dados.
2 - Adicionar despesas
3 - 
4 - 
'''))
        if(s == 1):
        	    Fina.ajuste()
        elif(s == 3):
        	    print("ok")
        elif(s == 2):
            Fina.novoDes()
            
        else:
            print("fim!")
        	
Fina.menu()

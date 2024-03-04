# Fazer uma calculadora 


class Calculadora():
    
    def somar(self):
        num1 = float(input("Informe seu numero: "))
        num2 = float(input("Informe seu numero: "))
        
        resultado = num1 + num2
        print(f"Resultado é {resultado}")
    
    def subtrair(self):
        num1 = float(input("Informe seu numero: "))
        num2 = float(input("Informe seu numero: "))
        
        resultado = num1 - num2
        print(f"Resultado é {resultado}")
    
    def dividir(self):
        num1 = float(input("Informe seu numero: "))
        num2 = float(input("Informe seu numero: "))
        
        resultado = num1 / num2
        print(f"Resultado é {resultado}")
        
    def multiplicar(self):
        num1 = float(input("Informe seu numero: "))
        num2 = float(input("Informe seu numero: "))
        
        resultado = num1 * num2
        print(f"Resultado é {resultado}")
    
    def executar_calculadora(self):
        while True:
            print("-----Menu Calculadora-----")
            print("1 - Somar")
            print("2 - Subtrair")
            print("3 - Dividir")
            print("4 - Multiplicar")
            print("5 - Sair")
            opcoes = {
                '1': self.somar,
                '2': self.subtrair,
                '3': self.dividir,
                '4': self.multiplicar,
                '5': exit
            }
            opcao = input("Digite sua opção: ")    
            if opcao in opcoes:
                if opcao == "5":
                    print("Saindo da Calculadora")
                    break
                else:
                    opcoes[opcao]()
            else:
                print("Opção Invalida")

cal = Calculadora()
cal.executar_calculadora()
                
        
                
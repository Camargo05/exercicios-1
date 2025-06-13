import sys

class ConversorTemperatura:
    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_para_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\n--- Conversor de Temperatura ---")
        print("1. Converter de Celsius para Fahrenheit")
        print("2. Converter de Fahrenheit para Celsius")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        
        if escolha == '1':
            try:
                temp_celsius = float(input("Digite a temperatura em Celsius: "))
                temp_fahrenheit = ConversorTemperatura.celsius_para_fahrenheit(temp_celsius)
                print(f"Resultado: {temp_celsius}°C equivale a {temp_fahrenheit:.2f}°F")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '2':
            try: 
                temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
                temp_celsius = ConversorTemperatura.fahrenheit_para_celsius(temp_fahrenheit)
                print(f"Resultado: {temp_fahrenheit}°F equivale a {temp_celsius:.2f}°C")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '3':
            print("Encerrando o programa. Até logo!")
            sys.exit()

        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
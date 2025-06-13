class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero não é permitida."
        return a / b


if __name__ == "__main__":
    calc = Calculadora()

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números.")
            continue

        print("\nEscolha a Operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")

        escolha = input("Digite sua escolha (1/2/3/4): ")

        if escolha == '1':
            resultado = calc.somar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif escolha == '2':
            resultado = calc.subtrair(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif escolha == '3':
            resultado = calc.multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif escolha == '4':
            resultado = calc.dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Escolha inválida. Por favor, tente novamente.")
            continue

        calcular_novamente = input("\nDeseja fazer outro cálculo? (s/n): ")
        if calcular_novamente.lower() != 's':
            break

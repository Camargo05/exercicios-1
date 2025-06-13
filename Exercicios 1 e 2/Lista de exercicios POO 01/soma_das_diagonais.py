import random

def soma_diagonais_matriz_quadrada():
    try:
        n = int(input("Digite a ordem da matriz quadrada (n): "))

        if n <= 0:
            print("A ordem da matriz deve ser um número positivo.")
            return

        matriz = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
        
        print(f"\nMatriz quadrada gerada ({n}x{n}):")
        for linha in matriz:
            print("\t".join(map(str, linha)))

        soma_principal = 0
        soma_secundaria = 0
        for i in range(n):
            soma_principal += matriz[i][i]
            soma_secundaria += matriz[i][n - 1 - i]
            
        print(f"\nA soma da diagonal principal é: {soma_principal}")
        print(f"A soma da diagonal secundária é: {soma_secundaria}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

soma_diagonais_matriz_quadrada()
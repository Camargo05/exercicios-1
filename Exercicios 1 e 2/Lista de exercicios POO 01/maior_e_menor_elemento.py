import random

def maior_menor_matriz():
    try:
        linhas = int(input("Digite o número de linhas (m): "))
        colunas = int(input("Digite o número de colunas (n): "))

        if linhas <= 0 or colunas <= 0:
            print("As dimensões devem ser números positivos.")
            return

        matriz = [[random.randint(0, 99) for _ in range(colunas)] for _ in range(linhas)]

        print(f"\nMatriz gerada ({linhas}x{colunas}):")
        for linha in matriz:
            print("\t".join(map(str, linha)))

        maior = matriz[0][0]
        menor = matriz[0][0]

        for linha in matriz:
            for elemento in linha:
                if elemento > maior:
                    maior = elemento
                if elemento < menor:
                    menor = elemento
        
        print(f"\nO maior elemento da matriz é: {maior}")
        print(f"O menor elemento da matriz é: {menor}")

    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")

maior_menor_matriz()
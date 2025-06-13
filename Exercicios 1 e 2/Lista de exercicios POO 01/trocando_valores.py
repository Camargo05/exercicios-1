class ValorContainer:
    def __init__(self, valor):
        self.valor = valor

def trocar_valores(ref_a, ref_b):
    print("\n... Executando a troca ...")
    ref_a.valor, ref_b.valor = ref_b.valor, ref_a.valor

def simular_troca_valores():
    try:
        valor_a = int(input("Digite o valor para o Objeto A: "))
        valor_b = int(input("Digite o valor para o Objeto B: "))
        obj_a = ValorContainer(valor_a)
        obj_b = ValorContainer(valor_b)

        print("\nValores ANTES da troca:")
        print(f"Objeto A: {obj_a.valor}")
        print(f"Objeto B: {obj_b.valor}")

        trocar_valores(obj_a, obj_b)

        print("\nValores DEPOIS da troca:")
        print(f"Objeto A: {obj_a.valor}")
        print(f"Objeto B: {obj_b.valor}")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")

simular_troca_valores()
class Numero:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial

    def imprimir_valor(self):
        print(f"O valor do atributo é: {self.valor}")

def manipular_objeto():
    meu_numero = Numero()
    meu_numero.valor = 42
    meu_numero.imprimir_valor()
    print(f"Endereço de memória (ID) do objeto: {id(meu_numero)}")
    
manipular_objeto()
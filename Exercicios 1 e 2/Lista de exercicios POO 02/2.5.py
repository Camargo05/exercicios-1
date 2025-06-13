preco_unitario = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))

valor_total = preco_unitario * quantidade
troco = dinheiro_recebido - valor_total

print(f"TROCO = {troco:.2f}")
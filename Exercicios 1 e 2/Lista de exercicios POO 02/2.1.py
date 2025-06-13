largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor_metro_quadrado = float(input("Digite o valor do metro quadrado: "))

area_terreno = largura * comprimento
preco_terreno = area_terreno * valor_metro_quadrado

print(f"Area do terreno = {area_terreno:.2f}")
print(f"Preco do terreno = {preco_terreno:.2f}")
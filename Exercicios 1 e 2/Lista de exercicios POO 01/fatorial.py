def fatorial_recursivo(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fatorial_recursivo(n - 1)

try:
  numero = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
  
  if numero < 0:
    print("O fatorial não está definido para números negativos.")
  else:
    resultado = fatorial_recursivo(numero)
    print(f"O fatorial de {numero} é {resultado}.")

except ValueError:
  print("Entrada inválida. Por favor, digite um número inteiro.")
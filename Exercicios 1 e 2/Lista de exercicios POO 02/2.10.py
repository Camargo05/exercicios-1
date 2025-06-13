duracao_total_segundos = int(input("Digite a duracao em segundos: "))

horas = duracao_total_segundos // 3600
resto = duracao_total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")
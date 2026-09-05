# Programa em Python de Consumo-Energia
# Autor: Wilian Godoy francisco

# Entrada

Aparelho = input("Informar qual o aparelho: ")
Potencia = float(input("Informar a potência do aparelho: "))
HoraDia = float(input("Infomar tempo médio de uso: "))

# Processamento - Calcular o consumo mensal em Kw/h
ConsumoMensal = (Potencia*HoraDia*30) / 1000

#Saída - Resultado do cálculo de consumo mensal em Km/h
print (f"Aparelho: {Aparelho}")
print (f"Consumo Estimado: {ConsumoMensal}")

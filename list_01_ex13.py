# Receba quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia
quantidade_kg = float(input("Digite a quantidade de alimento em kg: "))
consumo_diario = 50 # em gramas por dia
dias = (quantidade_kg * 1000) / consumo_diario
print("O alimento durará:", dias, "dias")
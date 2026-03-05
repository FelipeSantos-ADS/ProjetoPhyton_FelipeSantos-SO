# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3° ângulo
angulo1 = float(input("Digite o 1° ângulo: "))
angulo2 = float(input("Digite o 2° ângulo: "))
angulo3 = 180 - (angulo1 + angulo2)
print("O valor do 3° ângulo é", angulo3)
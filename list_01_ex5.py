# Receba os coeficientes A, B e C de uma equação do 2° grau (AX² + BX + C = 0) Calcule e mostre as raízes reais
# Considerar que a equação possui 2 raízes reais
A = float(input("Digite o valor de A: ")) 
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
# Cálculo de delta
delta = B**2 - 4*A*C
# Cálculo das raízes reais
x1 = (-B + delta**0.5) / (2*A)
x2 = (-B - delta**0.5) / (2*A)
print("Raiz 1: ", x1)
print("Raiz 2: ", x2)
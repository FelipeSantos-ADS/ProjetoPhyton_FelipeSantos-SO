# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa
cateto1 = float(input("Digite o valor do 1° cateto: "))
cateto2 = float(input("Digite o valor do 2° cateto: "))
hipotenusa = (cateto1**2 + cateto2**2)**0.5
print("Hipotenusa:", hipotenusa)
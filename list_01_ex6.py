# Receba os valores de x e y. Efetua a troca de valores e mostre seus conteúdos
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
print(f"Antes da troca: x = {x}, y = {y}")
x, y = y, x
print(f"Após a troca: x = {x}, y = {y}")
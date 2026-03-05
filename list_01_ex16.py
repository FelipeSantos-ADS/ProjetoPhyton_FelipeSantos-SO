# Calcule o salário líquido considerando horas, valor/hora, desconto e dependentes
horas = float(input("Horas trabalhadas: "))
valor_hora = float(input("Valor por hora: "))
desconto = float(input("Percentual de desconto: "))
dependentes = int(input("Número de dependentes: "))
salario_bruto = horas * valor_hora
salario_liquido = salario_bruto * (1 - desconto/100)
salario_final = salario_liquido + dependentes*100
print("Salário a receber:", salario_final)
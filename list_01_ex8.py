# Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a.m
deposito = float(input("Digite o valor do depósito: "))
rendimento = deposito * 0.013
valor_final = deposito + rendimento
print("Rendimento do mês:", rendimento)
print("Valor final após 1 mês:", valor_final)
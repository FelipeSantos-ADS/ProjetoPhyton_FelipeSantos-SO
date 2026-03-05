# Calcule a quantidade de litros gastos em uma viagem. O carro faz 12 km/l.
# Recebendo tempo e velocidade média
tempo = float(input("Digite o tempo em horas: "))
velocidade = float(input("Digite a velocidade em km/h: "))
distancia = tempo * velocidade
litros_gastos = distancia / 12
print("Litros gastos:", litros_gastos)
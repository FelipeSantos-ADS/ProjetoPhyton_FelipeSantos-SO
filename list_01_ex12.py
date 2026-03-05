# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
idade_futura = idade + 17
print("idade atual:", idade)
print("idade em 17 anos:", idade_futura)
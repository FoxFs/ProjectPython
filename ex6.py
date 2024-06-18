import datetime

ano_atual = datetime.date.today().year
ano = int(input("Digite o ano do seu nascimento: "))
idade = ano_atual - ano

if idade <= 9:
    print("MIRIM:", f"Nadador mirim com idade de {idade} anos")
elif 10 > idade <= 14:
    print("INFANTIL:", f"Nadador infantil com idade de {idade} anos")
elif 15 > idade <= 19:
    print("JUNIOR:", f"Nadador junior com idade de {idade} anos")
elif idade == 20:
    print("SÊNIOR:", f"Nadador sênior com idade de {idade} anos")
elif idade > 20:
    print("MASTER:", f"Nadador master com idade de {idade} anos")
else:
    print("Formato invalido!, digite dnv")
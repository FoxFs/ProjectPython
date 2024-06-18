import datetime

ano_atual = datetime.date.today().year
ano = int(input("Digite o ano do seu nascimento: "))
idade = ano_atual - ano

if idade == 18:
    print("Você terá que fazer alistamento militar, boa sorte :)")
elif idade < 18:
    print(f"Você não tem que se alistar, falta {18 - idade} anos")
else:
    print("Você ja passou do alistamento a anos, espero que tenha se dado bem!")
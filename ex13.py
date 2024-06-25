times = ("Flamengo","Bahia","Botafogo","São Paulo","Athletico-PR","Red Bull Bragantino","Palmeiras","Internacional","Cruzeiro","Atlético-MG","Fortaleza","Juventude","Grêmio","Vasco","Fluminense","Criciúma","Corinthians","Atlético-GO","Vitória","Cuiabá")

print("***" * 10)
print("Questão A: os 5 primeiros colocados ")
for t in times[:5]:
    print(f"{t}")

print("***" * 10)
print("Questão B: ultimos 4 times colocados em ordem alfabetica")
for t in sorted(times[-4:]):
    print(f"{t}")

print("***" * 10)
print("Questão C: a tabela com os times em ordem alfabetica")
for t in sorted(times):
    print(f"{t}, ", end="")
import random

ddd = int(input("digite o DDD:"))
def gerar_numeros_celulares():
    numeros = []
    for c in range(0, 8):
        n = random.randint(0, 9)
        numeros.append(n)
    print(f"({ddd}) 9",*numeros, sep='')

##interface:
a1 = int(input("Quantos numeros você quer? "))
for n in range(0, a1):
    gerar_numeros_celulares()
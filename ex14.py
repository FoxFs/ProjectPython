##criar um programa que crie numeros aleatorios e indique o menor e o maior entre eles
import random
num = []
n_maior = 0
n_menor = 100
quan = int(input("Quantos numeros você quer gerar? "))
for c in range(0, quan):
    numeros = random.randint(1, 50)
    if numeros > n_maior:
        n_maior = numeros
    if numeros < n_menor:
        n_menor = numeros
    num.append(numeros)

print("**" * 20)
print(f"lista organizada de menor para o maior: {num}")
print(f"O maior numero da lista é {n_maior}")
print(f"O menor numero da lista é {n_menor}")
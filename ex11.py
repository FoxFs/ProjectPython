print("Sequencia de fibonnaci")
print("**" * 15)
n = int(input("Digite a quantidade de termos: "))
n1 = 0
n2 = 1
print("{} -> {}".format(n1, n2), end="")
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(" -> {}".format(n3), end="")
    n1 = n2
    n2 = n3
    cont += 1
print(": Fim")
print("**" * 15)
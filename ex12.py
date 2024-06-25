print("MOSTRANDO NUMEROS POR EXTENSO")
n = int(input("Digite um numero de [0 a 20]: "))

Extensão = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

if n <= 20:
    print(f"seu numero escolhido foi [{n}] e ele é escrito assim [{Extensão[n]}]")
else:
    print("Eu só funciono de 0 a 20 senhor (;-;) ...vai com calma! ")
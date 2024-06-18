peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a altura: "))
IMC = peso / (altura * altura)

if 16 > IMC < 16.9:
    print("Muito abaixo do peso")
elif 17 > IMC < 18.4:
    print("Abaixo do peso")
elif 18.5 > IMC < 24.9:
    print("Peso normal")
elif 25 > IMC < 29.9:
    print("Acima do peso")
elif 30 > IMC < 34.9:
    print("Obesidade Grau 1")
elif 35 > IMC < 40:
    print("Obesidade Grau 2")
elif IMC > 40:
    print("Obesidade Grau 3")
else:
    print("Numero invalido! tente novamente.")
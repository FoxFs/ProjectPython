print("#### DESCUBRA O NOME DOS TRIANGULOS ####")

lado1 = float(input("Digite o primeiro lado do triangulo: "))
lado2 = float(input("Digite o segundo lado do triangulo: "))
lado3 = float(input("Digite o terceiro: "))

if lado1 == lado2 and lado2 == lado3:
    print("Triangulo Equilátero")
else:
    if lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
        print("Triangulo Isósceles")
    elif lado1 != lado2 != lado3:
        print("Triangulo Escaleno")
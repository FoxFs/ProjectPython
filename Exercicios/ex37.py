print("##### BEM VINDO AO CONVERSOR DE NUMEROS #####")
while True:
    print(" " * 10)
    num = int(input("Numero para ser convertido: "))

    print('''ESCOLHA UMA OPÇÃO:
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL
[x] SAIR''')

    Metodo = str(input("Escolha o Metodo: "))

    if Metodo == "x" or Metodo == "X":
        break

    elif Metodo == "1" or Metodo == "2" or Metodo == "3":
        
        if Metodo == "1":
            print("---" * 10)
            binario = bin(num)
            print("Seu numero convertido em binario foi {}".format(binario))

        elif Metodo == "2":
            print("---" * 10)
            octa = oct(num)
            print(f"Seu numero convertido em binario foi {octa}")

        elif Metodo == "3":
            print("---" * 10)
            hexa = hex(num)
            print(f"Seu numero convertido em binario foi {hexa}")


    else:
        print("Opção invalida!")
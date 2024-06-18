import random
pc = random.randint(1, 3)

print("BEM VINDO AO JOGO JOKENPÔ EM PYTHON")
print('''### ESCOLHA ENTRE AS OPÇÕES ###
[1] PEDRA
[2] PAPEL
[3] TESOURA
###################################''')
op = int(input("Digite o numero da sua opção: "))

if op == 1 or op == 2 or op == 3:
    #papel edition
    if op == 1 and pc == 2:
        print("Você perdeu! que pena, tente novamente")
    elif op == 2 and pc == 2:
        print("Não!! você empatou")
    elif op == 3 and pc == 2:
        print("Parabéns você venceu")
    else:
        ##pedra edition
        if op == 3 and pc == 1:
            print("Você perdeu! que pena, tente novamente")
        elif op == 1 and pc == 1:
            print("Não!! você empatou")
        elif op == 2 and pc == 1:
            print("Parabéns você venceu")
        else:
            ##tesoura edition
            if op == 2 and pc == 3:
                print("Você perdeu! que pena, tente novamente")
            elif op == 3 and pc == 3:
                print("Não!! você empatou")
            elif op == 1 and pc == 3:
                print("Parabéns você venceu")
    
    print(f"Você escolheu {op} e a maquina {pc}")

else:
    print("Numero invalido!")

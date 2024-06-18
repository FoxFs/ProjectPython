print('''#### Lista mercado #######
[1] Arroz.. R$12.50
[2] cenoura.. R$2.50
[3] beterraba.. R$4.50
[4] carne bovina.. R$34.00  
#################################''')

produtos = []
op = float(input("Digite suas opções ao carrinho: "))
if op == 1:
    produtos.append(12.50)
elif op == 4:
    produtos.append(34)
elif op == 2:
    produtos.append(2.50)
elif op == 3:
    produtos.append(4.50)    
else:
    print("Numero invalido!")
desk = input("Deseja adicionar um item[S/N]: ")

if desk in "Ss":
    while desk != "N" or "n":
        op = float(input("Digite suas opções ao carrinho: "))
        if op == 1:
            produtos.append(12.50)
        elif op == 4:
            produtos.append(34)
        elif op == 2:
            produtos.append(2.50)
        elif op == 3:
            produtos.append(4.50)
        else:
            print("Numero invalido!")
        desk = input("Deseja adicionar mais um item[S/N]: ")
        if desk in "Nn":
            break

print("[1] CARTÃO [2] A VISTA")
pag = int(input("Qual a forma de pagamento?"))

##Se for no cartâo
if pag == 1:
    print("[0] NENHUMA, [1] 2X PARCELAS, [2] 3X OU MAIS")
    parcela = int(input("Em quantas parcelas?? "))

    if parcela == 0:
        print("###"*15)
        desconto1 = sum(produtos) - (sum(produtos) * 5 / 100)
        print(f"o total a pagar será R${desconto1:.2f} reais")

    elif parcela == 1:
        print("###"*15)
        print(f"o total a pagar será R${sum(produtos):.2f} reais")

    elif parcela == 2:
        print("###"*15)
        juros = (sum(produtos) * 20 / 100) + sum(produtos)
        print(f"o total a pagar será R${juros:.2f} reais")

    else:
        print("Numero invalido!")

##Se for a vista
elif pag == 2:
    desconto2 = sum(produtos) - (sum(produtos) * 10 / 100)
    print("###"*15)
    print(f"o total a pagar será R${desconto2:.2f} reais")

else:
    print("Resposta invalida! tente dnv")

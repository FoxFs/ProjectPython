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

print("###"*15)
print(f"o total a pagar será R${sum(produtos):.2f} reais")
lista = ("Arroz", 12.50, "Frango", 34, "pilão")

if len(lista) % 2 != 0:
    raise ValueError("A lista està imcompleta!!!")

lista_supermercado = []
for i in range(0, len(lista), 2):
    produtos = lista[i]
    preço = lista[i + 1]
    lista_formatada = f"{produtos}...............R${preço:.2f}"
    lista_supermercado.append(lista_formatada)

print('''----------------------------------------------
            LISTA SUPERMERCADO
----------------------------------------------''')
for pos, l in enumerate(lista_supermercado):
    print(f"{pos+1}.{l}")
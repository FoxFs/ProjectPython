##medidor de escala cartografica
perg1 = int(input("Dê a largura do local a qual quer catalogar em metros(obs:so funciona em metros): "))
perg2 = int(input("De a medida gráfica: "))

D = int ((perg1 * 100) / perg2)
d = int (perg2 / perg2)

print(f"A escala cartográfica do terreno apresentado é de {d}:{D}")
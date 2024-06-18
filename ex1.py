#Variaveis 
cas = float(input("Digite o valor da casa: R$"))
sal = float(input("Qual o seu salario? R$"))
anos = int(input("Em quantos anos você pretende pagar? "))

parcela = cas / (anos * 12 )
minimo = sal * 30 / 100

#logica do programa
print(10 * "###")
if parcela <= (sal * 30/100):
    print("Emprestimo aprovado")
    print("Você pagará R${:.2f} por mês por {} anos".format(parcela, anos))

elif parcela > (sal * 30/100):
    print("emprestimo recusado")
    print("Você não conseguirá pagar a casa de R${:.2f} em parcelas de R${:.2f} por mês durante {} anos".format(cas, parcela, anos))
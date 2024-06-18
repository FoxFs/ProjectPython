nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if media < 5:
    print("REPROVADO", f"Media: {media}")
elif 5 > media < 6.9:
    print('RECUPERAÇÃO', f"Media: {media}")
elif media > 7.0:
    print("APROVADO", f"Media: {media}")
else:
    print("media invalida!, um dos numeros ou mais nâo correspondem a base (0.0 - 10.0) exigida")
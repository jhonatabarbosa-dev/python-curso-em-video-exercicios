aluno = {}
aluno["Nome"] = str(input("Nome: "))
aluno["Média"] = float(input(f"Média de {aluno["Nome"]}: "))

for chave, valor in aluno.items():
    print(f"{chave} é igual a {valor}")

if aluno["Média"] <= 6.9:
    print("Situação é igual a Reprovado")
else:
    print("Situação é igual a Aprovado")

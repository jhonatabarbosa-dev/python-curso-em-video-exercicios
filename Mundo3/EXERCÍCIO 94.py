continuar = "S"
cadastro = []
mediadeidade = media = 0

while continuar in "Ss":

    pessoa = {}

    pessoa["nome"] = input("Nome: ")
    pessoa["sexo"] = input("Sexo: [M/F] ")

    while pessoa["sexo"] not in "MmFf":
        pessoa["sexo"] = input("ERRO! Por favor, digite apenas M ou F: ")

    pessoa["idade"] = int(input("Idade: "))
    mediadeidade += pessoa["idade"]

    cadastro.append(pessoa)

    continuar = input("Quer continuar? [S/N] ")
    while continuar not in "SsNn":
        continuar = input("ERRO! Por favor, digite apenas S ou N: ")

media = mediadeidade / len(cadastro)

print()

print(f"A) Ao todo temos {len(cadastro)} pessoas cadastradas")
print()
print(f"B) A média de idade é de {media:.2f} anos")
print()
print("C) As mulheres cadastradas foram: ", end= "")

for pessoa in cadastro:
    if pessoa["sexo"] in "Ff":
       print(f"{pessoa["nome"]}", end = " ")

print()

print(f"D) Lista das pessoas que estão acima da média: ", end = "")
for pessoa in cadastro:
    if pessoa["idade"] >= media:
        print()
        for chave, valor in pessoa.items():
            print(f"{chave} = {valor}; ", end ="")

temp = [] #lista que guarda os nomes cadastrados
prin = [] #lista que guarda os pesos das pessoas cadastradas
c = "" #variável que guarda a resposta quando o usuário for perguntado se ele quer continuar
maior = menor = 0
while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso: ")))

    if len(prin) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    prin.append(temp[:])
    temp.clear()

    while True:

        c = str(input("Quer continuar? [S / N] \n"))

        if c not in "SsNn":
            print("Resposta Inválida!")

        if c in "Ss":
            break

        if c in "Nn":
            break

    if c in "Nn":
        break

print(f"Ao todo você cadastrou {len(prin)} pessoas. ", end = "")
print(f"O maior peso foi de {maior} quilos de ", end = "")

for p in prin:
    if p[1] == maior:
        print(f"{p[0]}, ", end = "")

print(f" e o menor peso foi {menor} quilos de ", end="")

for p in prin:
    if p[1] == menor:
        print(f"{p[0]}")

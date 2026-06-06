lista = []
continuar = ""

while True:
    valor = int(input("Digite um valor: "))

    if valor not in lista:
        lista.append(valor)

    else:
        print("Valor repetido! Não adicionado!")
    
    continuar = input("Quer continuar [s / n] ? ")

    if continuar in "Nn":
        break

print(f"Você digitou os números {sorted(lista)}")


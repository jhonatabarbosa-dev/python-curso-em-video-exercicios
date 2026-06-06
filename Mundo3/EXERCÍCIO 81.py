lista = []
continuar = descrescente = ""
contador = 0

while True:
    x = int(input("Digite um valor: "))
    lista.append(x)
    contador += 1
    continuar = (input("Quer continuar? [S / N] "))

    if continuar in "Nn":
        break

print(f"Você digitou {contador} elementos.")
print(f"Os valores em ordem decrescente são: {sorted(lista, reverse=True)}")

lista.count(5)

if lista.count(5) >= 1:
    print("O número 5 apareceu na lista")
else:
    print("O número 5 não apareceu na lista")

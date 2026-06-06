lista = []
par = []
impar = []
continuar = ""
while True:
    x=int(input("Digite um número: "))
    lista.append(x)

    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

    continuar = str(input("Quer continuar? "))

    if continuar in "Nn":
        break

print(f"A lista completa é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpares é {impar}")
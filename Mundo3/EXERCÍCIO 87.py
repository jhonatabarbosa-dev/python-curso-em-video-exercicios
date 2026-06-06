lista = [[], [], []]
par = []
coltres = []
somapar = somacoltres = maior = 0

for c in range (0,3):
    lista[0].append(int(input(f"Digite um valor para [0,{c}]: ")))
    if lista[0][c] % 2 == 0:
        par.append(lista[0][c])
    if c == 2:
        coltres.append(lista[0][2])

for c in range (0,3):
    lista[1].append(int(input(f"Digite um valor para [1,{c}]: ")))
    if lista[1][c] % 2 == 0:
        par.append(lista[1][c])
    if c == 2:
        coltres.append(lista[1][2])

for c in range (0,3):
    lista[2].append(int(input(f"Digite um valor para [2,{c}]: ")))
    if lista[2][c] % 2 == 0:
        par.append(lista[2][c])
    if c == 2:
        coltres.append(lista[2][2])

somapar = sum(par)
somacoltres = sum(coltres)

maior = max(lista[1])

print(f"{lista[0]} \n{lista[1]} \n{lista[2]}")
print(f"A soma dos pares é {somapar}")
print(f"A soma dos valores da terceira coluna é {somacoltres}")
print(f"O maior valor da segunda linha é {maior}")
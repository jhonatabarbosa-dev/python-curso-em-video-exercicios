lista = [[], [], []]
for c in range (0,3):
    lista[0].append(int(input(f"Digite um valor para [0,{c}]: ")))
for c in range (0,3):
    lista[1].append(int(input(f"Digite um valor para [1,{c}]: ")))
for c in range (0,3):
    lista[2].append(int(input(f"Digite um valor para [2,{c}]: ")))
print(lista[0])
print(lista[1])
print(lista[2])

valores = [[],[]]
a = par = impar = 0
for c in range (1,8):
    a = int(input(f"Digite o {c}º valor: "))
    if a % 2 == 0:
        valores[0].append(a)
    else:
        valores[1].append(a)

valores[0].sort()
valores[1].sort()

print(f"Os números pares digitados foram {valores[0]}")
print(f"E os números ímpares digitados foram {valores[1]}")

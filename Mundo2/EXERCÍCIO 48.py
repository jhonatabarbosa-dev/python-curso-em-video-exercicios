soma = 0
for c in range (1,501,2):
    print(c)
    multiplo = c % 3
    if multiplo == 0:
        soma = soma + c
print("A soma entre todos os múltiplos de 3 é",soma)
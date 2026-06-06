pares = 0
tupla = tuple(int(input("Digite um número: ")) for c in range(0, 4))
        
print(f"Você digitou os valores: {tupla}")

for c in range(0, 4):
    if tupla[c] % 2 == 0:
        pares += 1

nove = tupla.count(9)
print(f"O valor 9 apareceu {nove} vezes.")

if 3 in tupla:
    tres = tupla.index(3) + 1
    print(f"O valor 3 apareceu na {tres}ª posição.")
else:
    print("O valor 3 não foi digitado.")

print(f"Os valores pares digitados foram {pares}")
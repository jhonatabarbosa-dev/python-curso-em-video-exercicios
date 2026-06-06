from random import randint

selecionados = tuple(randint(0, 10) for c in range(0, 5))

print (selecionados)

maior = max(selecionados)
menor = min(selecionados)

print(f"O maior valor sorteado foi: {maior}")
print(f"O menor valor sorteado foi: {menor}")
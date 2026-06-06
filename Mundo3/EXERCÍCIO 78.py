valores = []
for c in range(0, 5):
    valores.append(int(input(f"Digite um valor na posição {c}: ")))
    
maior = max(valores)
menor = min(valores)

print(f"Os valores digitados foram {valores}")

print(f"O maior número digitado foi {maior} na posição {valores.index(maior)}, e o menor foi {menor} na posição {valores.index(menor)}.")

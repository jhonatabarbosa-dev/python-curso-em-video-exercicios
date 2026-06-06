brasileirao21 = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense")

print("-" * 90)

print("Os 5 primeiros colocados foram: ")

for c in brasileirao21 [0:5]:
        print(c, end = " ")

print()
print("-" * 90)        

print("Os 4 últimos colocados foram: ")

for c in brasileirao21 [16:]:
    print(c, end = " ") 

print()
print("-" * 90)    

print("Os times em ordem alfabética são: ")      
print(sorted(brasileirao21)) 

print("-" * 90)

print(f"A Chapecoense ficou em {brasileirao21.index("Chapecoense") + 1}º lugar")
    
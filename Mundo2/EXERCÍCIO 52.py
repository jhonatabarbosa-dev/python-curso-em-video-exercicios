contador = 0
n=int(input("Digite um número: "))
for c in range (1,n + 1):
    if n % c == 0:
        contador = contador + 1

if contador == 2:
    print("Vc digitou {} e ele é um número primo".format(n))
else:
    print("Vc digitou {} e ele não é um número primo".format(n))

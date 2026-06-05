soma=0
cont = 0

for c in range (1,7):
    n=int(input("Digite o {}º número: ".format(c)))

    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n
print(" ")
print("Vc digitou {} números pares, e a soma entre eles é {}".format(cont,soma))





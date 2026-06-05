continuar = "s"
contador = soma = media = maior = menor = 0

while continuar != "n":
    
    n = int(input("Digite um número: "))
    
    contador += 1
    soma += n
    media = soma / contador

    if contador == 1 :
        maior = n
        menor = n

    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    continuar = input(("Quer continuar? "))      

    if continuar == "n":
        print ("Você digitou {} números, e a média entre eles é {:.1f}. ".format(contador, media), end = "")
        print ("O maior valor digitado foi {} e o menor foi {}.".format(maior, menor))
        break
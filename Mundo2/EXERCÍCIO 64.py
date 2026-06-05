parar = 999
n = soma = c = 0
while True:

    while n != parar:
        n = int(input("Digite um número [999 para parar]: "))
        soma += n
        c += 1

        if n == parar:
            c += -1
            soma -= 999
            print("Você digitou 999! Programa finalizado!", end = " ")
            print("Você digitou {} números, e a soma entre eles é {}".format(c,soma))
            break
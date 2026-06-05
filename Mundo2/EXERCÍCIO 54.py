ano=0
contadorma = 0
contadorme = 0

for i in range (1,8):
    ano=int(input("Em que ano nasceu a {}ª pessoa? ".format(i)))

    maioridade = 2025 - ano

    if maioridade < 21:
        contadorme = contadorme + 1

    elif maioridade >= 21:
        contadorma = contadorma +1

if contadorma >= 1 and contadorme>= 1:
    print("{} pessoas são de maior, e {} pessoas são de menor".format(contadorma,contadorme))
elif contadorma >=1 and contadorme == 0:
    print("{} pessoas são de maior, e ninguém é de menor".format(contadorma))
elif contadorma == 0 and contadorme >= 1:
    print("Ninguém é de maior e {} pessoas são de menor".format(contadorme))
while True:
    v1 = float(input("Digite o 1° número: "))
    v2 = float (input("Digite o 2º número: "))

    x=str(input("Escolha o que fazer \n[1] Somar \n[2] Multiplicar \n[3] Maior ou Menor \n[4] Novos Números \n[5] Sair do Programa \n"))

    m1 = 0
    m2 = 0

    if x == "1":
        print("{} + {} = {}".format(v1,v2,(v1 + v2)))
    elif x == "2":
        print("{} x {} = {}".format(v1,v2,(v1 * v2)))

    m1 = v1 - v2
    m2 = v2 - v1

    if x == "3" and m1 > m2:
            print("O maior entre {} e {} é {}.".format(v1,v2,v1))
    elif x == "3" and m2 > m1:
        print("O maior entre {} e {} é {}.".format(v1, v2,v2))
    elif x == "3" and m1 == m2:
        print("{} e {} são número iguais".format(v1,v2))
    elif x == "4":
        print ("Digite novos números")

    elif x == "5":
        print("Fim do Programa")
        break

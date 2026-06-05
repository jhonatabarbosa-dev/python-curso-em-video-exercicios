n=int(input("Digite um número: "))
print("Qual operação vc quer fazer? \n1 [+] Adição \n2 [-] Subtração \n3 [*] Multiplicação \n4 [/] Divisão")
print(" ")
operacao=input("Escolha: ")


for c in range (1,11):
    if operacao == "1":
        print("{} + {} = {}".format(n,c,(n + c)))

    elif operacao == "2":
        print("{} - {} = {}".format(n,c,(n - c)))

    elif operacao == "3":
        print("{} x {} = {}".format(n,c,(n * c)))

    elif operacao == "4":
        print("{} / {} = {}".format(n,c,(c % n)))
    else:
        print("Opção Inválida!")

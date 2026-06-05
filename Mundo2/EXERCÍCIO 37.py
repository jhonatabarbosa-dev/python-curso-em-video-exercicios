n=int(input("Digite um número: "))

opcao=int(input("Vc quer converter esse número para: \n[1] binário \n[2] octal \n[3] hexadecimal \n "))

if opcao == 1:
    print("O número {} em binário é {}".format(n, (bin (n)[2:])))

elif opcao == 2:
    print("O número {} em octal é {}".format(n,(oct(n)[2:])))

elif opcao == 3:
    print("O nímero {} em hexadecimal é {}".format(n,(hex(n)[2:])))
else:
    print("Opção iválida! Tente novamente>")





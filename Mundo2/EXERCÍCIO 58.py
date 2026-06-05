import random
n=random.randint(0,10)
cont = 1

print("PENSEI EM UM NÚMERO ENTRE 0 E 10! SERÁ QUE VC É CAPAZ DE ACERTAR? ")
print("------------------------------------------------------------------")

chance=int(input("QUAL É O NÚMERO QUE EU PENSEI? "))

while chance != n:
    print("VC ERROU TENTE DE NOVO")
    chance = int(input("QUAL É O NÚMERO QUE EU PENSEI? "))
    cont = cont + 1

if chance == n:
    print("PARABÉNS!! O NÚMERO ERA {} VC VENCEU DEPOIS DE {} TENTATIVAS!!".format(n,cont))
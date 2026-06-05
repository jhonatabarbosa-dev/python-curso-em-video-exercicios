import random
n=random.randint(0,5)
print("ACERTE O NÚMERO")
print("--------------------------------------------------------------------------------------")
print("PENSEI EM UM NÚMERO ENTRE 0 E 5! SERÁ QUE VC É CAPAZ DE ACERTAR? EU ACHO QUE NÃO HAHHA")
print("--------------------------------------------------------------------------------------")
print("VC SÓ TEM UMA CHANCE!")
print("--------------------------------------------------------------------------------------")
chance1=int(input("QUAL É O NÚMERO QUE EU PENSEI? "))
if chance1 != n:
    print("--------------------------------------------------------------------------------------")
    print("ERROU!! O NÚMERO ERA {}!! VC PERDEU!!!".format(n))
else:
    print("--------------------------------------------------------------------------------------")
    print("PARABÉNS!! O NÚMERO ERA {} VC VENCEU!!".format(n))
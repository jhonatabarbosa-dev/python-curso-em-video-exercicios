n1=float(input("Qual a primeira nota? "))
n2=float(input("Qual a segunda nota? "))

m = (n1 + n2) / 2

if m < 5.0:
    print("MÉDIA {}, REPROVADO!".format(m))
elif m >= 5.0 and m < 7.0:
    print("MÉDIA {}, RECUPERAÇÃO!".format(m))
else:
    print("MÉDIA {}, APROVADO!".format(m))


s=float(input("Qual é o seu salário? R$ "))

aumento= (s * 15) / 100

if s <= 1250.00:
    print("Com o aumento de 15% seu novo salário será de {:.2f}".format(s + aumento))

if s > 1250.00:
    aumento = (s * 10) / 100
    print("Com o aumento de 10% seu novo salário será de {:.2f}".format(s + aumento))
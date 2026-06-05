salario=float(input("Qual o seu salário? R$ "))
print("Com 15% de aumento seu novo salário é de R${:.2f} reais.".format( salario + (salario*15) / 100 ))
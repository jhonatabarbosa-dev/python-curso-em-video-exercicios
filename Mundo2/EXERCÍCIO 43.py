peso=float(input("Qual seu peso? Kg "))
altura=float(input("Qual a sua altura? "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Seu IMC é {:.1f}, vc está ABAIXO DO PESO".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu IMC é {:>1f}, vc tem o PESO NORMAL".format(imc))
elif imc >= 25 and imc < 30:
    print("Seu IMC é {:.1f}, vc tem SOBREPESO".format(imc))
elif imc >=30 and imc < 40:
    print("Seu IMC é {:.1f}, vc tem OBESIDADE".format(imc))
else:
    print("Seu IMC é {:.2f}, vc tem OBESIDADE MÓRBIDA".format(imc))
ano=int(input("Qual o ano de nascimento do(a) atlleta? "))
idade = 2025 - ano


if idade < 10:
    print("O(a) atleta tem {} anos, é um(a) atleta Mirim".format(idade,ano))
elif idade >=10 and idade < 15:
    print("O(a) atleta tem {} anos, é um(a) atleta Infantil".format(idade,ano))
elif idade >= 15 and idade < 20:
    print("O(a) atleta tem {} anos, é um(a) atleta Júnior".format(idade,ano))
elif idade == 20:
    print("O(a) atleta tem {} anos, é um(a) atleta Sênior".format(idade,ano))
else:
    print("O(a) atleta tem {} anos, é um(a) atleta Master".format(idade,ano))
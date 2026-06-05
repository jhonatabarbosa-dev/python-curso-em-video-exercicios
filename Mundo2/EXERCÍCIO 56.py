somadeidade = 0
contador = 0
maisvelho = 0
quem = " "
for c in range (1,5):
    nome=str(input("Qual o nome da {}ª pessoa? ".format(c))).upper().strip()
    idade=int(input("Qual é sua idade? "))
    sexo=str(input("Qual o seu sexo? [M/F] ")).upper()
    somadeidade = somadeidade + idade
    if sexo == "M":
        maisvelho = idade
        quem =nome
        if idade > maisvelho:
            maisvelho = idade
            quem = nome
    if sexo == "F" and idade < 20:
        contador = contador + 1
print("A média de idade do grupo é de {:.2f} anos".format(somadeidade / 4))
print("O homem mais velho é {}, ele tem {} anos".format(quem,maisvelho))
print("Há {} mulheres com menos de 20 anos".format(contador))

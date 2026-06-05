continuar = ""
homem = maiordeidade = mulher = 0

while True:
    idade=int(input("Qual sua idade? "))
    sexo=str(input("Qual seu sexo [m / f]? "))

    if idade > 18:
        maiordeidade += 1

    if sexo == "m":
        homem += 1

    if sexo == "f" and idade < 20:
        mulher += 1   

    continuar = str(input("Quer continuar? [s / n]")) 

    if continuar == "n":
        print(f"{maiordeidade} pessoas tem mais de 18 anos, {homem} homens foram cadastrados, {mulher} mulheres tem menos de 20 anos ")
        break
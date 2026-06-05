c = 1
while c != 0:
    s=str(input("Qual o sexo da pessoa? [M/F] ")).upper()
    if s == "M" or s == "F":
        print("FIM")
    elif s != "M" and s != "F":
        print("Resposta inválida!")
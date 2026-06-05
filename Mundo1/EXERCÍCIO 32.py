ano=int(input("Em que ano estamos? "))
bi= (ano % 4)
if bi == 0:
    print("Este ano é bissexto")
else:
    print("Esse ano não é bissexto")
import random

print("[1] Pedra \n[2] Papel \n[3] Tesoura")
escolha=input("Escolha: ")

pc=random.choice (("pedra", "papel", "tesoura: "))

if pc == "pedra" and escolha == "3":
    print("Eu esolhi {} e vc escolheu {}, VC PERDEU!!".format("pedra","tesoura"))
elif pc == "pedra" and escolha == "2":
    print("Eu escolhi {}, e vc escolheu {}, VC GANHOU!!".format("pedra","papel"))

elif pc == "papel" and escolha == "1":
    print("Eu escolhi {} e vc escolheu {}, VC PERDEU!!".format("papel","pedra"))
elif pc == "papel" and escolha == "3":
    print("Eu escolhi {} e vc escolheu {}, VC GANHOU!!".format("papel","tesoura"))

elif pc == "tesoura" and escolha == "2":
    print("Eu escolhi {} e vc escolheu {}, VC PERDEU!!".format("tesoura","papel"))
elif pc == "tesoura" and escolha == "1":
    print("Eu escolhi {} e vc escolheu {}, VC GANHOU!!".format("tesoura","pedra"))
else:
    print("Escolhemos igual,empate!")








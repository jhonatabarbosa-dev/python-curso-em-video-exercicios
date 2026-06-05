contador = 0
while True:

    import random

    opcao_do_pc = ""
    resultado = 0
    aleatorio = random.randint(0, 10)
    opcao_do_jogador = (input("Você escolhe par ou ímpar? [p / i] "))

    if opcao_do_jogador == "i":
        opcao_do_pc = "p"
        print("Ok, eu fico com par! ", end = "")

    elif opcao_do_jogador == "p":
        opcao_do_pc = "i"
        print("Ok, eu fico com ímpar! ", end = "")

    n = int(input("Agora escolha seu número!! "))

    resultado = aleatorio + n

    if resultado % 2 == 0 and opcao_do_jogador == "p" and opcao_do_pc == "i" :
        contador += 1
        print(f"Como vc pediu par e jogou {n}, e eu joguei {aleatorio}, e {aleatorio + n} é par VC VENCEU!!")

    elif resultado % 2 != 0 and opcao_do_jogador == "i" and opcao_do_pc == "p" :
        contador += 1
        print(f"Como vc pediu ímpar e jogou {n}, e eu joguei {aleatorio}, e {aleatorio + n} é ímpar VC VENCEU!!")

    else:

        if resultado % 2 == 0 and opcao_do_jogador == "i" and opcao_do_pc == "p" :
            print(f"Como vc pediu ímpar e jogou {n}, e eu joguei {aleatorio}, e {aleatorio + n} é par então EU VENCI!!", end = "")

        elif resultado % 2 != 0 and opcao_do_jogador == "p" and opcao_do_pc == "i" :
            print(f"Como vc pediu par e jogou {n}, e eu joguei {aleatorio}, e {aleatorio + n} é ímpar então EU VENCI!!", end = "")
        print(f" Fim do programa! Você venceu {contador} vezes")
        break
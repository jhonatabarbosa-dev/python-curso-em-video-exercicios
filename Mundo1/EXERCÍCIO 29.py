vel=int(input("Qual era a velocidade do carro?: "))
if vel > 80:
    print("Você foi multado")
    multa=(vel - 80) * 7
    print("Sua multa será  de {}".format(multa))
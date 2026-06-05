nasc=int(input("Em que ano vc nasceu? "))
ano=int(input("Em que ano nós estamos? "))
a = ano - nasc

if a < 18:
    print("Vc tem {} anos, ainda faltam {}a pra vc se alistar".format(a,(18 - a)))
elif a == 18:
    print("Vc tem {} anos, já está na hora de vc se alistar!".format (nasc,))
else:
    print("Vc tem {} anos, já passou {}a de vc se alistar".format(a,(a - 18)))
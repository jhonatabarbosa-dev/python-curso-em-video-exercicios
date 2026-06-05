import math

angulo=float(input("Digite o ângulo: "))
seno=math.sin(math.radians(angulo))
print("O seno de {}, é {:.2f}".format(angulo, seno))
cosseno=math.cos(math.radians(angulo))
print("O cosseno de {}, é {:.2f}".format(angulo,cosseno))
tangente=math.tan(math.radians(angulo))
print("A tangente de {}, é {:.2f}".format(angulo,tangente))

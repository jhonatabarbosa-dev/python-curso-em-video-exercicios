import random
from random import shuffle
n1=(input("PRIMEIRO NOME: "))
n2=(input("SEGUNDO NOME: "))
n3=(input("TERCEIRO NOME: "))
n4=(input("QUARTO NOME: "))
ordem = [n1,n2,n3,n4]
random.shuffle(ordem)
print("A ORDEM DE APRESENTAÇÃO SERÁ")
print(ordem)
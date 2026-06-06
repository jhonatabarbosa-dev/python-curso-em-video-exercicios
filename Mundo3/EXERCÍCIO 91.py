from random import randint
from time import sleep
from operator import itemgetter

jogo = {"jogador 1": randint(1,6),
        "jogador 2": randint(1,6),
        "jogador 3": randint(1,6),
        "jogador 4": randint(1,6)}

ranking = {}

print("Valores Sorteados: ")

for chave, valor in jogo.items():
    print(f"{chave} tirou {valor} no dado")
    sleep(1)

ranking = sorted(jogo.items(),key=itemgetter(1), reverse =True)
print()
print("Ranking dos Jogadores")
for i, v in enumerate(ranking):
    print(f"{i + 1}º lugar: {v[0]} com {v[1]} pontos")
    sleep(1)

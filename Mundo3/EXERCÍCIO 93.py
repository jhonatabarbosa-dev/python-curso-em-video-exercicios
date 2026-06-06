jogador= {}

jogador ["nome"] = str(input("Nome do jogador: "))
jogador["partidas"] = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))

gols = []

for c in range (1,jogador["partidas"] + 1):
    gols.append(int(input(f"Quantos gols na partida {c}? ")))

jogador["gols"] = gols[:]

jogador["total"] = sum(gols)
print()

print(jogador)
print()

for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}")
print()

print(f"O jogador {jogador ["nome"]} fez {len(jogador["gols"])} partidas.")
for indice, valor in enumerate(jogador["gols"]):
    print(f"-> Na partida {indice + 1} fez {valor} gols")
print(f"Foi um total de {jogador["total"]} gols")

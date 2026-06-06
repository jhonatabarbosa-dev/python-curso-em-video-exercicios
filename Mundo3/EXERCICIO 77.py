palavra = ("alface","caderno","cachorro","guitarra","Jesus","casa")

for p in palavra:
    print(f"\nNa palavra {p.upper()} temos ",end="")
    for letra in p:
        if letra.lower () in "aeiou":
            print(letra, end = " ")
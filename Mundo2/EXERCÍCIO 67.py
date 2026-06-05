while True:
    c = t = n = 0
    n = int(input("Quer ver a tabuada de qual valor? "))

    if n < 0 :
        break
    
    while c <= 9:
        c += 1
        t = n * c

        print(f"{n} x {c} = {t}")

print("Programa tabuada encerrado, volte sempre!")        
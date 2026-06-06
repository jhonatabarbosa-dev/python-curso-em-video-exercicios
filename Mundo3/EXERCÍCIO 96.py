def calculo(l,c):
    area = l * c
    print(f"A área de um terreno {l} x {c} é de {area:.2f}m²")


l=float(input("LARGURA (m): "))
c=float(input("COMPRIMENTO (m): "))
calculo(l,c)
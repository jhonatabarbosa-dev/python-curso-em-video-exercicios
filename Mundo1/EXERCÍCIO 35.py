a=float(input("Lado A do Triangulo: "))
b=float(input("Lado B do Triangulo: "))
c=float(input("Lado C doTriangulo: "))

if a + b > c and a + c > b and b + c > a:
    print("Isso forma um triangulo")
else:
    print("Isso não forma um triangulo")
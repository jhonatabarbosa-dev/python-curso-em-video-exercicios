a=float(input("Lado A do Triangulo: "))
b=float(input("Lado B do Triangulo: "))
c=float(input("Lado C do Triangulo: "))

if a + b > c and a + c > b and b + c > a:
    print("Isso forma um triangulo",end=" ")
    if a == b and b == c:
        print("equilátero",end=" ")
    elif a == b and b != c or a == c and a != b or b == c and b != a :
        print("isósceles",end=" ")
    elif a != b and b != c and a != c:
        print("esacaleno")
else:
    print("Isso não forma um triangulo")



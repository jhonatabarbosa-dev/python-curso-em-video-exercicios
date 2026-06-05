salto = 0
n1=int(input("Digite um número: "))
razao=int(input("Razão: "))
print("Os 10 primeiros termos da razão de {} são: {} -> ".format(n1,n1), end=' ')
c = 1
while c < 10:
    salto = n1 + razao
    n1 = salto
    c = c + 1
    print(salto, "-> ", end=' ')
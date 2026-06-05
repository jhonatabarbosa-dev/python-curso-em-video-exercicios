pt = int(input("Primeiro Termo: "))
ra = int(input("Razão da PA: "))
print(pt)
c = 1 

while c < 10:
    pt = pt + ra 
    c += 1
    print (pt) 

while True:

    termos = int(input("Quantos termos a mais você vai querer? (Digite 0 para encerrar o programa) "))

    c += termos

    if termos != 0:

        while termos != 0:
            pt = pt + ra
            termos -= 1
            print(pt)

    elif termos == 0:
        print("Programa finalizado!, foram mostrados {} termos ao todo.".format(c))
        break        
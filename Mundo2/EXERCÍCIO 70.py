total = maisdemil = 0
maisbarato = 10000000
nomebarato = continuar = produtomaisbarato = ""
while True:
    produto=str(input("Nome do produto: "))
    preco=float(input("Preço do produto: R$ "))

    if preco < maisbarato:
        maisbarato = preco
        produtomaisbarato = produto

    total += preco

    if preco > 1000:
        maisdemil += 1

    continuar = input("Quer continuar [s / n]? ")

    if continuar == "n":
        print(f"O total gasto na compra foi R${total:.2f}. {maisdemil} produtos custam mais de R1000,00 reais, e o produto mais barato é o(a){produtomaisbarato}.")
        break
        
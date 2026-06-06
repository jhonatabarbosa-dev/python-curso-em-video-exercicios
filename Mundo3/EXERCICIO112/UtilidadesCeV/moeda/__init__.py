def linha():
    return "-" * 30

def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res

def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return res

def dobro(preco):
    res = preco * 2
    return res

def metade(preco):
    res = preco / 2
    return res

def resumo(preco,aum, dim):
    res1 = preco + (aum * preco / 100)
    res2 = preco - (dim * preco / 100)

    return (f"{linha()}\n"
            f"{"RESUMO DO VALOR".center(30)}\n"
            f"{linha()}\n"
            f"Preço analisado: \t{moeda(preco)}\n"
            f"Dobro do preço: \t{moeda(dobro(preco))}\n"
            f"Metade do preço: \t{moeda(metade(preco))}\n"
            f"{aum}% de aumento: \t{moeda(res1)}\n"
            f"{dim}% de redução: \t{moeda(res2)}\n"
            f"{linha()}")

def moeda(preco=0, moeda = "R$"):
    return f"{moeda} {preco:.2f}".replace(".",",")
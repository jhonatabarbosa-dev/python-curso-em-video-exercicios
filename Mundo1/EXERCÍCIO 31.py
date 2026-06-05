d=int(input("Sua viagem será de quantos Km? "))

preco=(d * 0.50)

if d <= 200:
    print("Sua viagem será de {} Km, sua passagem custrá {:.2f}".format(d,preco))
elif d > 200:
    preco=(d * 0.45)
    print("Sua viagem será de {} Km, sua passagem custará {:.2f}".format(d,preco))
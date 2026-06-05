preco=float(input("Qual o preço do produto? R$ "))
print(" ")
print("Qual a forma de pagamento?\n[1] A vista no dinheiro/cheque \n[2] A vista no cartão \n[3] Em até 2x no cartão \n[4] 3x ou mais no cartão \n")
print(" ")
pag=input("Digite sua opção: ")

total = 0

if pag == "1":
    print("Vc tem 10% de desconto!")
    total = 10 * preco / 100
    print(" ")
    print("Vc irá pagar R$ {:.2f}".format(preco - total))

elif pag == "2":
    print("Vc tem 5% de desconto!")
    total = 5 * preco / 100
    print(" ")
    print("Vc irá pagar R$ {:.2F}".format(preco - total))

elif pag == "3":
    print("Preço normal")
    print(" ")
    print("Vc irá pagar R$ {:.2F}".format(preco))

elif pag == "4":
    print("20% de juros!")
    total = 20 * preco / 100
    print(" ")
    print("Vc irá pagar no total R$ {:.2F}".format(preco + total))
else:
    print("Opção inválida! Tente Novamente!!")








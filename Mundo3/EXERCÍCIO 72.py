x = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

n = numero = 0

while True:
    n = int(input("Digite um número entre zero e vinte: "))

    if n < 0 or n > 20:
        print("Erro!" , end = " ")

    if n >= 0 and n <= 20:
        break

numero = x[n]
print(f"Você digitou {numero}")

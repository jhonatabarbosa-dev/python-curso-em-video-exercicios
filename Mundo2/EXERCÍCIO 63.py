print("Sequência de Fibonacci")
print("----------------------")
n = int(input("Quantos termos você quer nessa sequência? "))

final = 3

primeiro = 0
segundo = 1
terceiro = primeiro + segundo 

print("{} {} {}".format(primeiro, segundo, terceiro),end = " ")

while final < n :
    final += 1
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo
    print(terceiro, end = " ")
c = total = 0

saque = int(input("Quanto você quer sacar? R$ "))

total = saque

cedula_atual = 50  # Começamos pela maior cédula
total_cedulas = 0  # Contador de cédulas por valor

while True:
    # Se o valor atual do saque ainda suporta a cédula atual
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedulas += 1
    else:
        # Se houve cédulas entregues, imprime o resultado
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de R${cedula_atual}")
        
        # Lógica para trocar o valor da nota
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        
        total_cedulas = 0  # Reseta o contador para a próxima nota
        
        if total == 0:
            break

print("=" * 30)
print("Saque finalizado com sucesso!")
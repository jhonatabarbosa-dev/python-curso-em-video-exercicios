casa=float(input("Qual o valor da casa? R$ "))
salario=float(input("Qual o salário do(a) comprador(a)? R$ "))
parcelamento=int(input("Em quantos anos você vai pagar sua casa? "))

pagamento = casa / (parcelamento * 12)
porcentagem = 30 * salario / 100


if pagamento > porcentagem:
    print("Pra pagar uma casa de R${} sua prestação mensal será de R${:.3f},EMPRÉSTIMO NEGADO!".format(casa,pagamento))
elif pagamento <= porcentagem:
    print("Pra pagar uma casa de R${} sua prestação mensal será de R${:.3f} EMPRÉSTIMO ACEITO!".format(casa,pagamento))






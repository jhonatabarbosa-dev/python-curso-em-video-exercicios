from datetime import datetime
ano_atual = datetime.now().year
cadastro = {}
cadastro["nome"] = str(input("Nome: "))
cadastro["idade"] = int(input("Ano de nascimento: "))
cadastro["clt"] = int(input("Carteira de trabalho (Digite 0 (ZERO) caso não tenha): "))
if {cadastro["clt"]} != 0:
    cadastro["contratação"] = int(input("Ano de contratação: "))
    cadastro["salário"] = float(input("Salário: R$ "))
    cadastro["aposentadoria"] = (cadastro["idade"] + cadastro["contratação"] + 35 - ano_atual)
for chave, valor in cadastro.items():
    print(f"- {chave} tem o valor {valor}")

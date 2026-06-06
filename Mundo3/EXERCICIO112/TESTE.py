from EXERCICIO112.UtilidadesCeV import moeda
from EXERCICIO112.UtilidadesCeV import dado

p = dado.leiadinheiro("Digite um preço: R$")
print(moeda.resumo(p, 35, 22))

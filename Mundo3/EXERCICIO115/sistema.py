from EXERCICIO115.lib.interface import *
from EXERCICIO115.lib.arquivo import *
from time import sleep

arq = "CursoemVideo.txt"

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastrar nova pessoa","Sair do Sistema"])
    if resposta == 1:
        #opção de listar conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #opção de cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema...até logo")
        break
    else:
        print("\033[31mErro! Digite uma opção válida!\033[m")

    print("\033[3mCarregando sistema...\033[0m")
    sleep(2)

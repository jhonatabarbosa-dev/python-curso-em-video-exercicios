def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print("\n\033[0;31mO usuário interrompeu o programa\033[m")
            return 0
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            entrada = input(msg).replace(",", ".")
            n = float(entrada)
        except KeyboardInterrupt:
            print("\n\033[0;31mO usuário interrompeu o programa\033[m")
            return 0
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número real válido!\033[m")
            continue
        else:
            return n



nInt = leiaInt("Digite um número inteiro: ")
nFloat = leiaFloat("Digite um número real: ")
print(f"Você acabou de digitar o número inteiro => [{nInt}] e o número real => [{nFloat}]")


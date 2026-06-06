def voto(nasc: int):
    from datetime import date
    hoje: int = date.today().year
    obrigatorio: int = hoje - nasc

    if obrigatorio >= 16 and obrigatorio < 18 or obrigatorio >= 65:
        return f"Com {obrigatorio} anos o voto é opcional."
    elif obrigatorio < 16:
        return f"Com {obrigatorio} anos não vota"
    elif obrigatorio >= 18 and obrigatorio <= 64:
        return f"Com {obrigatorio} anos o voto é obrigatório"


ano_nasc = int(input("Em que ano você nasceu? "))

print(voto(ano_nasc))


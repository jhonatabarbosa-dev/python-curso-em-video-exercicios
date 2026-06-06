listagem = ("Guitarra Cort Mutility II bag" ,7.585, "Pedaleira Valeton GP 200" ,2.501, "Placa de áudio PreSonus Studio 26c" ,1.989, "Fone In-ear Sennheiser IE 100 PRO" ,1.241)

print("-" * 50)
print("LISTA DE EQUIPAMENTOS DE JHONATA BARBOSA")
print("-" * 50)

for c in range (0,8,2):
    print(f"{listagem[c]:-<40}",f"R$ {listagem[c + 1]}" )
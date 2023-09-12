nome = range(1, 10)
for i, valor in enumerate(nome):
    print(f'Chave {i} e Valor {valor}')
    if input("Parar?") == "s":
        print("Cancelando..")
        break

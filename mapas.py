"""
Mapas
  - Complemento de Dicionarios
Conhecidos em python como dicionarios
Dicionarios em Python são representados por chaves {}

"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionarios

for chave in receita:
    print(chave)  # Imprime as chaves

for chave in receita:
    print(receita[chave])  # Imprime os valores

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

print(receita.keys())  # Retorna um dicionario de chaves

# Acessando as chaves (Modo 'Pythonico')

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores (Modo 'Pythonico')

print(receita.values())  # Retorna um dicionarios de valoes

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionarios

print(receita.items())  # Retorna um tupla doas chaves e valores
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

"""
Módulo Collections - Counter
Collections -> High-performance Container Datetypes
Counter -> Contador

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo Collections Counter
que é parecido com um dict (dicionario) contendo como chave o elemento da lista passada como
parametro e como valor a quantidade de ocorrencias desse elemento

"""

# Importar o Counter
from collections import Counter

# Podemos utilizar qualquer iteravel, lista, dicionario, conjuntos
lista = ["Erick", 1, 1, 2, 3, 2, 3, 3, 3, 4, 2, 4, 5, 5, 2, 4, 1, 5, 2, 45, 45, 66, 3, 2, 1]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)  # Counter({2: 6, 1: 5, 3: 5, 4: 3, 5: 3, 45: 2, 66: 1})
# Cada elemento da lista o Counter cria uma chave e conta a quantidade de ocorrências no valor

# Exemplo 2
print(Counter('Geek University'))
# é contado as ocorrencias de cada caractere

# Exemplo 3
texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of 
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing 
software like Aldus PageMaker including versions of Lorem Ipsum."""

palavras = texto.split()  # Faz a separação das palavras
print(palavras)

res = Counter(palavras)  # Conta quantas vezes cada palavra aparece no texto
print(res)
print(res.most_common(5))  # Filtar as 5 palavras que mais aparecem

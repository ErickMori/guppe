"""
Loop for

loop -> Estrutura de repetição
for -> Uma dessas estruturas

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis
Exemplos de iteraveis:
- String
    nome = "geek university"
-Lista
    lista = [1, 3, 5, 7, 9]
-Range
    numero = range[1, 10]
"""

nome = 'Geek Univesity'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)
#range(valor_inicial, valor_final)

#Exemplo de for 1 (Iterando sobre uma String
for letra in nome:
    print(letra)

#Exemplo de for 2 - Iterando sobre uma Lista
for numero in lista:
    print(numero)

#Exemplo de for 3 - Iterando sobre um Range
for numero in range(1, 10):
    print(numero)

for numero in numeros:
    print(numero)

nome = 'Geek Univesity'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

"""
enumerate: Cria uma tupla
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k').....)
"""
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

#Descartar o indice pois só precisamos da letra
#O o underline descarta o valor
for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    #imprime o indice e valor
    print(valor)
    #imprime o indice
    print(valor[0])
    #imprimi o valor
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

#Impressão do loop na mesma linha: mudar o padrão end='\n' para end=''
nome = 'Geek University'
for letra in nome:
    print(letra, end='')

"""
Table de Emoticons unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""
#Origin: U+1F60D
#Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 10):
        print('\U0001F60D' * num)
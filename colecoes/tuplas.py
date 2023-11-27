"""
Tuplas (tuple)

São bastante parecidas com listas.
Existem basicamente duas diferenças:

1 - As tuplas são representadas por parenteses ()
2 - As tuplas são imutáveis, isso é, ao se criar uma tupla ela não muda.
    Toda operação em uma tupla gera uma nova tupla

# Métodos para adição, remoção de elementos nas tuplas NÃO existem, dado o fato de tuplas serem imutáveis
# Soma*, Valor Máximo*, Valor Minimo* e Tamanho
    * Somente se todos valores forem inteiros ou reais
# Porque utilizar tuplas?
    - São mais rápidas do que listas, performance maior de velocidade
    - Deixam o código mais seguro, devido ser imutável


    #Cuidada 1:
    As tuplas são representadas por (), mas veja:
    tupla1 = (1, 2, 4, 5, 6)
    print(tupla1)
    print(type(tupla1)) #Retorna type=tupla

    tupla2 = 1, 2, 3, 4, 5, 6      # Tambem é uma tupla
    print(tupla2)
    print(type(tupla2)) #Tambem retorna uma tupla

    #Cuidado 2:

    tupla3 = (4)      # Não é uma tupla, o python considera apenas o int
    print(tupla3)
    print(type(tupla3)) # retorna type=int

    tupla4 = (4,)      # Este é uma tupla devido a virgula
    print(tupla4)
    print(type(tupla4)) # retorna type=tuple

    tupla5 = 4,      # Este tambem é uma tupla devido a virgula
    print(tupla5)
    print(type(tupla5)) # retorna type=tuple

    #Conclusao: podemos concluir que tuplas são definidas pela virgula e não pelo uso do parenteses

# Podemos gerar uma tupla dinamicamente com o range()

tupla1 = tuple(range(11))
print(tupla1)
print(type(tupla1))

# Desempactocamento de tupla - Gera erro (valueError) se colocarmos um numero diferente de elementos para desempacotar

tupla2 = ('Geek University', 'Programação Python')
escola, curso = tupla2
print(escola)
print(curso)

tupla3 = (1, 2, 3, 4, 5, 6)
print(sum(tupla3), end=' ')
print(max(tupla3), end=' ')
print(min(tupla3), end=' ')
print(len(tupla3), end=' ')

# Concatenação de tuplas
tupla4 = (1, 2, 3)
print(tupla4)
tupla5 = (4, 5, 6)
print(tupla5)
print(tupla4 + tupla5)
print(tupla4)
print(tupla5)

# Tuplas são imutaveis mas podemos sobreescrever seus valores
tupla4 = tupla4 + tupla5
print(tupla4)

# Procurar determinado elemento contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)


"""

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)
for indice, n in enumerate(tupla):
    print(indice, n)

# Contando elementos dentro de uma tupla

tupla1 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla1.count('a')) # Retorna 2

escola = tuple('Geek University')
print(escola.count('e')) # Retorna 3

# Dicas na utilização de tuplas
# - Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo em Listas que não precisam ser modificadas
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Acesso de elementos da tupla também é semelhante a lista, por index

print(meses[5])

# Iterar com while

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificar em qual indice um elemento esta na tupla

print(meses.index('Junho'))
print(meses.index('Junho', 3)) # Pesquisa a partir do index 3

# Slicing tupla[inicio:fim:passo]

print(meses[5::2])

# Copiando uma tupla

tupla = (1, 2, 3)
nova = tupla # Na tupla não temos o problema de SHALLOW COPY


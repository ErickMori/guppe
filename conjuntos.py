"""
Conjuntos

Conjutos em linguagem de programação, estamos fazendo referencia a teroria dos conjuntos da matematica

No Python os conjuntos são chamados de Sets
Da mesma forma que na matematica:
- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados

Conjuntos podem ser utilizados quando precisamos armazenar elementos mas não nos
importamos com a ordenação deles, quando não precisamos se preocupar com chaves,
valores e itens duplicados

Conjuntos (Sets) são referencias em Python com chaves {}

Diferenças entre conjuntos (sets) e Mapas (dicionarios) em Python:
    - Um dicionario tem chave/valor
    - Um conjunto tem apenas valor
    - Um conjunto não possui ordem dos elementos

Assim como todos outros conjunto Python, podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}

Podemos iterar em um set normalmente
for valor in s:
    print(valor)

"""
# Definindo um conjunto
# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Existem valores repetidos
print(s)  #
print(type(s))

# Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo é ignorado,
# Não retornara erro e não fará parte do conjunto

# Forma 2 (mais comum)

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

s = set('Geek University')
print(s)  # Ira remover as repetições

# Converter para conjunto (funciona com lista, tupla, dicionarios)

lista = [1, 2, 3, 4, 4, 5, 6, 6]
print(lista)
print(set(lista))

if "a" in s:
    print('Tem o a')
else:
    print('Não tem o a')

# Importante lembrar que alem de não termos valores duplicados, Não temos ordem.

lista = [99, 2, 34, 23, 23, 12, 1, 44, 44, 5]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = (99, 2, 34, 23, 23, 12, 1, 44, 44, 5)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# O dicionario por estar utilizando os elementos como chaves, não repetira tambem
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 34, 23, 23, 12, 1, 44, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Usos interessantes com Sets

cidades = ['BH', 'SP', 'CG', 'CI', 'CG', 'SP', 'CI']
print(cidades)
print(len(cidades))

# Filtrar quantas cidades distinta
setc = set(cidades)
print(setc)
print(len(setc))

# Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4)  # Como é um valor repedido, é ignorado (sem erros)
print(s)

# Remover elementos em um conjunto
# Forma 1
s.remove(3)  # Não é indice, é o próprio valor (conjuntos não possuem indices)
# Se não existir o valor, ira retornar KeyError
print(s)

# Forma 2
s.discard(2)  # Mesma funcao do remove() porém não retorna nenhum erro se não encontrar
print(s)

# Copiando um conjunto para outro
s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)  # O conjunto s se mantem, não é alterado com o novo.add(4)

# Forma 2 - Shallow Copy

novo = s
novo.add(4)
print(novo)
print(s)  # O conjunto s é modificado ao utilizar novo.add(4)

# Remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos matematicos de conjuntos
# Imagine que temos 2 conjuntos, um contendo estudantes do curso Python
# e outro contendo estudantes do curso de Java

estudantesPython = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantesJava = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Os cursos possuem alguns alunos em comum
# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 = Utilizando union (recomendado)

unicos1 = estudantesPython.union(estudantesJava)  # Poderia ser o contrario, mesmo resultado
print(unicos1)

# Forma 2 = Utilizando caractere pipe "|"

unicos2 = estudantesPython | estudantesJava
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantesPython.intersection(estudantesJava)
print(ambos1)

# Forma 2 - Utilizando &
ambos2 = estudantesPython & estudantesJava
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso - utilizando difference
so_python = estudantesPython.difference(estudantesJava)
print(so_python)

so_java = estudantesJava.difference(estudantesPython)
print(so_java)

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

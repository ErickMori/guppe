"""
Listas (list)

Funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINAMICOS
e também de podermos colocar QUALQUER tipo de dado

Obs: Linguagens C/Java: Arrays:
    -Possuem tamanho e tipo de dado fixo, ou seja, se você criar um array do tipo int e com tamanho 5,
    este array será sempre do tipo int e sempre no maximo 5 valores

    - DINAMICO em Python: Não possuem tamanho Fixo, ou seja, podemos criar a lista e adicionar elementos
    - QUALQUER tipo de dados: Não possuem tipo de dado Fixo, ou seja, podemos criar qualquer tipo de dado

    As listas em Python são representadas por colchetes []

"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

lista9 = [1, 2.34, True, 'Geek', 'd', [1, 3, 9], 45345345345]

# Checar se determinado valor esta contido na lista

num = 1
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

letra = 'e'
if letra in lista5:
    print(f'Encontrei o letra {letra}')
else:
    print(f'Não encontrei o letra {letra}')

# Podemos facilmente ordenar uma lista (obs: é possível ordenar lista de string também
lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(27))
print(lista5.count('e'))

# Adicionar elementos em lista

""" Para adicionar elementros em lista utilizamos a função append() 
Obs: com append() só é possivel adicionar 1 elemento por vez"""
print(lista1)
lista1.append(49)
print(lista1)

"""Possivel incluir com o append() uma lista dentro da lista"""
lista1.append([821, 874, 544])
print(lista1)

if [821, 874, 544] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrada')

"""Para adicionar como elementos separados utilizar extend()"""
lista1.extend([123, 55, 24])
print(lista1)

lista1.extend('Geek')
print(lista1)

"""Inserir elemento na lista informando a posição do indice utilizando insert(posição, valor)"""

lista1.insert(2, 'Novo valor')
print(lista1)

"""Concatenar duas listas"""

lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)

"""Imprimir lista reversa"""

lista1.reverse()
print(lista1)

print(lista1[::-1])

"""Copiar uma lista"""
lista7 = lista4.copy()
print(lista7)

"""Contar quantidade de elementos na lista utilizando len() """
print(len(lista5))

"""Remover o ultimo elemento de uma lista utilizando pop() 
o pop() também retorna o valor do elemento removido
Podemos remover um elemento pelo indice pop(2)"""
print(lista5)
lista5.pop()
print(lista5)
lista5.pop(2)
print(lista5)

"""Remover todos os elementos, zerar a lista utilizando clear()"""
lista5.clear()
print(lista5)

""" é Possivel Multiplicar elementos da lista [1, 2, 3] se torna [1, 2, 3, 1, 2, 3, 1, 2, 3]"""
lista8 = [1, 2, 3]
lista8 = lista8 * 3
print(lista8)

"""Converter string para lista"""
# Exemplo 1 com spli() - Separa os elementos da string pelo espaço entre elas
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2 com spli(caracter_desejado) - Separa os elementos da string pelo caracter desejado
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

"""Converter lista para string utilizando 'string ou espaco'. join()"""
curso = '-'.join(curso)
print(curso)

"""Iterando sobre lista"""
# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 = Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

""" Utilizando variaveis em listas """
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

""" Em listas fazemos acesso aos elementos de forma indexada """
#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # Verde

""" Fazer acesso aos elementos de forma indexada inversa """
print(cores[-2])  # Azul

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

""" Gerar indice em um for """

for indice, cor in enumerate(cores):
    print(indice, cor)

""" Encontrar o indice de um elemento na lista utilizando index(valor_procurado)
-> caso não encontre o valor_procurado, sera retornado erro
-> se houver duplicidade do valor_duplicado ele retorna o primeiro indice (primeiro encontrado)"""

carros = ["Uracan", "911", "Veyron", "Regera", "Uracan"]
encontrado = carros.index("Veyron")
print(f'Carro encontrado {encontrado}')

# procurar a partir de index predefinido index(valor_procurado, index_inicial)

print(carros.index("Uracan", 1))

# procurar dentro de um range predefinido index(valor_procurado, index_inicial, index_final)

print(carros.index("Uracan", 1, 5))

""" Trabalhando com slice de lista com parametros de inicio ou fim """

sequencia = [1, 2, 3, 4, 5, 6]
print(sequencia[1:])  # Iniciando no index 1 até todos os elementos restantes
print(sequencia[:2])  # começa no index 0 e vai até o index 2
print(sequencia[1:3])  # comeca no index 1 e vai até o index 3

# Utilizar o passo do slice na lista

print(sequencia[1::2])  # Começa no index 1 e vai até o final de 2 em 2
print(sequencia[::2])  # Começa no index 0 e vai até o final de 2 em 2
print(sequencia[4::-1])  # Comeca no index 4 e vai até o 0 de 1 em 1

""" Inverter valores em uma lista (o melhor é utlizar o reverse(), mas o codigo abaixo funciona """
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

""" Soma*, Valor maximo*, Valor minimo*, tamanho 
* Somente para valores inteiros ou reais"""

numerais = [1, 2, 3, 4, 5, 6]
print(sum(numerais))  # Soma
print(max(numerais))  # Valor maximo
print(min(numerais))  # Valor minimo
print(len(numerais))  # Tamanho da lista

""" Transformar uma lista em tupla """
print(numerais)
print(type(numerais))

tupla = tuple(numerais)
print(tupla)
print(type(tupla))

""" Desempacotamento de lista 
se tiver quantidade de valor na lista diferente de variaveis para receber, retornará erro"""
lista9 = [1, 2, 3]
num1, num2, num3 = lista9

print(num1)
print(num2)
print(num3)

""" Copiando uma lista para outra (shallow copy e deep copy)"""
""" DEEP COPY """
lista10 = [1, 2, 3]
print(lista10)

nova = lista10.copy()  # cópia
print(nova)

nova.append(4)
print(lista10)
print(nova)

# Ao utilizar o copy() copiamos os dados da lista para uma nova lista e elas ficaram totamente independentes,
# ou seja, modificando uma lista não afeta a outra, isso em Python é DEEP COPY (cópia profunda)

""" SHALLOW COPY """
lista11 = [1, 2, 3]
print(lista11)

nova2 = lista11  # cópia
print(nova2)

nova2.append(4)  # aqui será modificado a lista11 e a nova2
print(lista11)
print(nova2)

# Ao não utilizar o copy(), ambas as listas foram modificadas, após inserir o valor na nova2 foi inserido
# o mesmo valor na lista11, isso em Python é SHALLOW COPY (cópia raza)
# Tomar cuidado com SHALLOW COPY, pois pode alterar lista que você não quer alterar

# Teste criado por mim
"""
    resposta = ''
    check = False
    while check != True:
    resposta = int(input("Digite o valor: "))
    if(resposta in lista4):
        print(f'Numero {resposta} encontrado!')
        check = True
    else:
        print(f'Numero {resposta} não encontrado!')
"""

"""
Ranges

-Precisamos conhecer o loop for para usa os ranges
-Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória,
mas sim de maneira especificada, sequenciada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

"""
#Exemplo 1
for num in range(11):
    print(num, end='')

#Exemplo 2 range(valor_inicio, valor_parada)
for num in range(4, 11):
    print(num, end='')

#Exemplo 3 range(valor_inicio, valor_parada, passo)
#OBS: Passo especificado

for num in range(1, 10, 2):
    print(num, end='')

#Exemplo 4 range(valor_inicio, valor_parada, passo)
#OBS: range INVERSO

for num in range(11, 0, -1):
    print(num)

#Formar um lista (array) do range, funções list()
lista = list(range(10))
print(lista)
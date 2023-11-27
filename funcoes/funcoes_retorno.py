"""
Funcoes com retorno

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros)  # Print não retorna nada
print(f'Retorno de print: {ret_pr}')

OBS: Em python quando uma função não retorna valor, o retorno é None
    Utilizar a palavra reservada "return" para retornar um valor

OBS: "return":
    1 - Ela finaliza a função, ou seja, ela sai da execução da função
    2 - Podemos ter em uma função diferentes returns (mas apenas 1 irá retornar)
    3 - Podemos retornar qualquer tipo de dado e até mesmo multiplos valores

"""


# Exemplo função

def quadrado_de_7():
    print(7 * 7)


quadrado_de_7()  # O print não retorna, ele imprime em tela
ret = quadrado_de_7()
print(f'Retorno: {ret}')  # Ira retornar NONE pois o print não retorna valor


# Refatorar a função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f'Retorno correto: {ret}')  # Agora sim ira retornar o valor da função

print(f'Retorno correto: {quadrado_de_7() + 1}')  # Aqui a função retorna dentro do print e soma + 1


# Refaturando a primeira função

def diz_oi():
    return "Oii"


print(diz_oi())


def diz_oi2(nome):
    return "Olá " + nome + "!"
    print('Executado após o retorno')  # Esta linha não é executada pois esta após o return


alguem = "Erick"
print(diz_oi2(alguem))


# Exemplo 2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()  # Ira atribuir os valores da funcao para cada variavel (desempacotar)
print(num1, num2, num3, num4)
print(outra_funcao())  # Aqui é impresso a tupla (2, 3, 4, 5)


# Exemplo 3 - Funcao para jogar uma moeda
# importar biblioteca random de python e a funcao 'random' dela
from random import random

def joga_moeda():
    #Gera um numero pseudo-randomico entre 0-1
    valor = random()
    if valor > 0.5:  # no lugar da variavel valor poderia ser colocado direto a funcao random()
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

#  Erros comuns na utilização de retorno

"""
# Não precisamos do 'else' no caso abaixo, basta inserir na linha abaixo de execução
# Pois o return encerra a função!
def eh_impar(numero):
    if numero % 2 != 0:
        return True
    else:
        return False
"""

def eh_impar(numero):
    if numero % 2 != 0:
        return True
    return False

print(eh_impar(5))

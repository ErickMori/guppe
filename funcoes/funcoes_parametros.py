"""
Funções com Parametro (de entrada)

- Funções que recebem dados para serem processador dentro da mesma.

"""

# Refatorar 1
"""
def quadrado_de_7():
    return 7 * 7
"""


def quadrado(numero):
    return numero * numero  # ou numero ** 2 (elevado a 2)


print(quadrado(7))

ret = quadrado(5)
print(ret)

# Refatorar 2
"""
def cantar_parabens():
    print('Parabens para você')
    print('nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')
    
"""


def cantar_parabens(aniversariante):
    print('Parabens para você')
    print('nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')


cantar_parabens("Erick")

# Funções com mais de 1 parametro


def soma(a, b):
    return a + b


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(5,3))
print(outra(3, 2, 'Geek '))

# Obs: Se informado um numero errado de parametros ou argumentos teremos um TypeError

# Nomeando parametros

def nome_completo(string1, string2):  #utilizar nome e sobrenome ao invés de string1 e string2
    return f'Seu nome completo é {string1} {string2}'


print("Erick", "Silva")

# Diferença entre parametros e argumentos
# Parametros são variaveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# Argumentos nomeados (Keyword arguments)
# Caso utilizamos nomes dos parametros nos argumentos para informa-los, podemos
# utilizar qualquer nome

print(nome_completo(string2='Mori', string1='Ezio'))
# Aqui você informa exatamente qual argumento esta informando

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total  # O return finaliza a função, portanto precisa estar fora do for (num in numero):


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))
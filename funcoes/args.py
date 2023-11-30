"""
Entendendo o *args

- O *args é um parametro como outro qualquer (entrada).
    Isso significa que voce podera chamar de qualquer coisa desde que comece com asterisco

Exemplo:
*xis

Mas por convenção, utilizamos *args para defini-lo

O que é o *args:

O parametro *args utilizados em uma função coloca os valores extras informados como
entrada em um tupla. Então desde ja lembre-se que tuplas são imutaveis

"""

# Exemplos
# Função sem *args


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))
# print(soma_todos_numeros(4, 6))  # Falta 1 parametro, retorna TypeError
# print(soma_todos_numeros(4, 6, 9, 8))  # 1 parametro a mais, retorna TypeError


# Função com *args utilizando for


def soma_todos_numeros_args(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_todos_numeros_args())
print(soma_todos_numeros_args(1))
print(soma_todos_numeros_args(1, 6))
print(soma_todos_numeros_args(1, 6, 9))


# Refatorando Função com *args utilizando sum


def soma_todos_numeros_args2(nome, sobrenome, *args):
    return sum(args)


print(soma_todos_numeros_args2('Erick', 'Silva'))
print(soma_todos_numeros_args2('Erick', 'Silva', 1))
print(soma_todos_numeros_args2('Erick', 'Silva', 1, 6))
print(soma_todos_numeros_args2('Erick', 'Silva', 1, 6, 9))

# Outros exemplos


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Quem é voce?'


print(verifica_info())   # Retorna 'Quem é voce?'
print(verifica_info(1, True, 'University', 'Geek'))  # Retorna 'Bem vindo Geek'
print(verifica_info(1, 'University', 3))  # Retorna 'Quem é voce?'

# Desempacotar (lista, tupla, conjunto) com args


def soma_todos(*args):
    return sum(args)


numeros = [1, 6, 8, 9, 10]
print(soma_todos(*numeros))  # Basta inserir o asteriscos para desempacotar

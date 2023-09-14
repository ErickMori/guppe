"""
Módulo Collections - Default Dict

# Recapitulando dicionario
dicionario = {'curso': 'Programação e Python Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['nao_existe'])  # KeyError

Obs: Lambdas são funções sem nome que pode ou não receber
parametros de entrada e retornar valores
"""


# No default dict não ira retornar o KeyError caso a chave não exista, é retornado o default
# utilizando um lambda para isso.

# Import do Default dict
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = "Programação e Python Essencial"
print(dicionario)
print(dicionario['nao_existe'])  # Não ira retornar erro devido o defaultdict
print(dicionario)  # a chave nao_existe é criada com o valor 0

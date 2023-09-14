"""
Módulo Collections: Ordered Dict

É um dicionario que garante a ordem de inserção dos elementos

"""
# Em um dicionario a ordem de inserção dos elementos não é garantida
dicionario1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for chave, valor in dicionario1.items():
    print(f'chave={chave}:valor={valor}')

# No OrderedDict ele garante que a biblioteca ira manter a ordem
# importar ordered dict

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

# Entendendo a diferença entre dict e OrderedDict

# Dicionarios comums:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # Retorna True porque no dicionario comum a ordem não importa

# Ordered Dict
o_dict1 = OrderedDict({'a': 1, 'b': 2})
o_dict2 = OrderedDict({'b': 2, 'a': 1})
print(o_dict1 == o_dict2)  # Retorna False porque no OrderedDict a order importa!

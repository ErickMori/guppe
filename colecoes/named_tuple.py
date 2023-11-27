"""
Módulo Collections - Named Tuple

#Recap tupla
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple (Tupla nomeada) -> São tuplas diferenciadas onde
especificamos um nome para a mesma e também parametros

"""

# Importando
from collections import namedtuple

# Precisamos definir o nome e parametros.

# Forma 1
#   cachorro = namedtuple('cachorro', 'idade raca nome')  # 3 parametros separados por espaço

# Forma 2
#   cachorro = namedtuple('cachorro', 'idade, raca, nome')  # 3 parametros separados por virgula

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])  # 3 parametros em lista (recomendada)

# Usando a tupla

ray = cachorro(idade=2, raca='Chow-chow', nome='Ray')
print(ray)
print(ray[1])  # Acessando por indice
print(ray.nome)  # Acessando por nome (recomendado e óbvio a se usar)

print(ray.index('Chow-chow'))  # Retorna o indice do 'Chow-chow
print(ray.count('Chow-chow'))  # Conta quantas vezes o 'Chow-chow' aparece

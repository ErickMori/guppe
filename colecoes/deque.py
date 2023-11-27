"""
Módulo Collections - Deque

O Deque é uma lista de alta performance

"""

# Importação
from collections import deque

# Criando um deque

deq = deque('ee')
print(deq)

# Adicionando elementos no deque

deq.append('k')  # Adiciona ao final do deq
print(deq)

deq.appendleft('G')  # Adiciona ao inicio do deq
print(deq)

# Recomendo elementos

print(deq.pop())  # Remove o ultimo elemento
print(deq)

print(deq.popleft())  # Remove o primeiro elemento
print(deq)

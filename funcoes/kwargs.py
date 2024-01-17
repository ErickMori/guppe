"""
**kwargs

o nome kwargs é uima convenção, pode ser chamado por qualquer nome
seguinte dos 2 asteristicos: ex: **nome **parametros


O **kwargs exige que utilizemos parametros nomeados e transforma esses
parametros extras em um dicionario

"""
# Exemplo 1
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print (f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(erick='Verde', julia='Amarelo', fernando='Azul', vanessa='Branco')
# Obs: O parametros *args e **kwargs NÃO SÃO OBRIGATORIOS

cores_favoritas()
cores_favoritas(geek='Navy')

# Exemplo 2

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é..'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))

# Nas nossas funções podemos ter (NESTA ORDEM):
# - Parametros obrigatorios
# - *args
# - Parametros default (nao obrigatorio)
# - **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(31, 'Erick')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Fernando', solteiro='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda porque manter esta ordem dos tipos de parametros

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

"""
a = 1
b = 2
args = (3,1)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
"""

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))  # Utilizar duplos asterisco para desempacotar o dicionario

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)  # 1 Asterisco lista
soma_multiplos_numeros(*tupla)  # 1 Asterisco tupla
soma_multiplos_numeros(*conjunto)  # 1 Asterisco conjunto

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)  # 2 Asterisco para dict

# Obs: Os nomes da chave em um dicionario devem ser os mesmos dos parametros da função



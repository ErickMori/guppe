"""
Funções com parametros padrão (default parameters)

- Funções onde a passgem de parametro é opcional
"""

print('Geek University')
print()  # Informar o texto é opcional (a função print tem o parametro opcional)


# Exemplo de função com parametro o
def exponencial(numero, potencia=2):  # O padrao de potencia sera igual a 2
    return numero ** potencia


print(exponencial(2, 3))  # Eleva a potencia informada
print(exponencial(3, 2))  # Eleva apotencia informada

print(exponencial(3))  # Por padrao eleva ao quadrado

# OBS:  Os parametros com valor default DEVEM sempre estar depois dos sem padrão
# Exemplo ERRADO:
#   def errado(num=2, potencia):
#   return num ** potencia
# Exemplo CORRETO:


def correto(potencia, num=2):
    return num ** potencia

# Exemplo mais complexo


def mostra_info(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Ola {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))  # Precisa utilizar o Keyword do parametro, pois 'instrutor' não é o 1º
print(mostra_info('Geek', True))
print(mostra_info('Erick'))

# Porque utilizar parametros com valor default
# - Flexibilidade nas funções
# - Evita erros com parametros incorretos
# - Permite trabalhar com com exemplos mais legiveis de código

# Tipos de dados que podem ser utilizados como default do parametro:
# - TODOS (numero, string,floats, bool, listas, tuplas, dicit, funções, etc)

# Funções como parametros


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))  # Por padrao esta chamando a funcao soma
print(mat(2, 2, subtracao))  # Solicita a funcao subtracao

# Escopo - Evitar problemas e confusoes

# Variaveis globais
# Variaveis locais

instrutor = 'Geek'  # Variavel Global ( não esta dentro de algum escopo )

def diz_oi():
    instrutor = 'Python'  # A variavel local sobrepoe a global
    return f'Oi {instrutor}'  # A variavel instrutor esta fora do escopo

print(diz_oi())

# A variavel local sobrepoe a global

def diz_ola():
    prof = 'Geek'  # Variavel local
    return f'Ola {prof}'

print(diz_ola())
#print(prof)  # Erro pois a variavel prof é local, não pode ser acessada de fora

# OBS: Tentar evitar variaveis globais
"""
total = 0

def incremental():
    total = total + 1  # Erro Variavel local nao inicializada
    return total

print(incremental())

"""

total = 0

def incremental():
    global total  # Avisando que queremos utilizar a variavel global
    total = total + 1  # Erro Variavel local nao inicializada
    return total

print(incremental())
print(incremental())
print(incremental())

# Podemos ter funções que são declaradas dentro de função e tambem forma especial de escopo de variavel

def fora():
    contador = 0
    def dentro():
        nonlocal contador  # nonlocal chama a variavel da função de cima
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
#print(dentro())  # Não funciona chamando de fora da funcao fora()
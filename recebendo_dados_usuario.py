"""
Recebendo dados do usuario

input() = Todo dado recebido via input é do tipo String

"""
#Entrada de dados
#print("Qual seu nome?")
#nome = input() #Entrada

nome = input('Qual seu nome?')

# Exemplo de print 'antigo' 2.x
#print('Seja bem-vindo(a) %s' % (nome))

#Exemplo de print 'moderno' 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

#Exemplo de print 'mais recente' 3.7
print(f'Seja bem-vindo(a) {nome}')

#print("Qual sua idade?")
#idade = input() #Entrada

idade = int(input('Qual sua idade?'))
#Processamento

# Saida de dados
# Exemplo de print 'antigo' 2.x
#print('O %s tem %s anos' % (nome, idade))

# Exemplo de print 'antigo' 2.x
#print('O {0} tem {1} anos'.format(nome, idade))

#Exemplo de print 'moderno' 3.x
print(f'O {nome} tem {idade} anos')
"""
int(idade) = cast
Cast é a conversao de um tipo de dado para outro
"""
print(f'O {nome} nasceu em {2023 - idade}')
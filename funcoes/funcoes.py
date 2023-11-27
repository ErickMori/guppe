"""
Funções

- Funcções são pequenos trechos de código que realizam tarefas especificas
- Pode ou não receber entradas de dados e retornar uma saida de dados
- Uteis para executar procedimentos similares por repetidas vezes

Obs: Ao escrever uma função que realiza varias tarefas dentro dela é
recomendado fazer uma verificação para que a função seja simplificada
ou seja, cada função deve realizar apenas 1 tarefa (recomendado)

principio DRY - Don't Repeat Yourself

- Exemplo de funções simples nativas (Built-in): print() len() max() min() count(), etc

"""

# Exemplo de utilização de funções
# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando função integrada (Built-in) do Python print()
# print(cores)

# curso = 'Programação em Python: Essencial'
# print(curso)

# cores.append('roxo')
# print(cores)

# cores.clear()  # função clear() não precisa enviar nenhum tipo de parametro dentro de ()
# print(cores)

# Definindo funções

"""
Em python a forma geral de definir uma funcao é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> SEMPRE com letras minúsculas e se for composto separado por underline (snake case)
parametros_de_entrada -> OPCIONAIS (conforme necessidade), caso tenha mais de um é separado por virgula
bloco_da_funcao -> Também chamado de corpo da função, onde o processo acontece, neste bloco pode
ter ou não o retorno da função

OBS: Para definir uma função é utilizado a palavra reservada 'def'
o bloco_da_função é aberto após dois pontos ':' que é utilizado em Python para 
definir blocos.
"""


def diga_oi():
    print('Oi!')


"""
OBS:
1 - Dentro de uma função pode ser utilizada outras funcoes
2 - A função acima só executa 1 uma tarefa (recomendado)
3 - A função acima não recebe nenhum parametro de entrada ()
4 - A função acima não retorna nada, ela apenas faz o print()
"""

# Chamada da funcao
diga_oi()

"""
ATENÇÃO AO CHAMAR A FUNCAO, NECESSARIO UTILIZAR O () AO EXECUTA-LA
"""


# Mais exemplos

def cantar_parabens():
    print('Parabens para você')
    print('nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


for n in range(3):
    cantar_parabens()

# Podemos criar variaveis do tipo de uma função e executar esta função atraves da variavel


canta = cantar_parabens  # não precisa do () neste caso, caso muito incomum (Não recomendado)
canta()  # a variavel canta se for a funcao (Não recomendado)

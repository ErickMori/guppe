"""
Dicionarios (dict)

Obs: em algumas linguagens de programação os dicionarios python são conhecidos por MAPAS

Dicionários são coleções do tipo chave/valor
Dicionarios são representados por chaves {}
Podemos utilizar qualquer tipo de dado (int, float, string, boolean, lista, tupla) como chaves de dicionarios

print(type({})) # Retorna type = dict


"""
# Forma 1 - Mais Comum

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 - Menos Comum

# paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
# print(paises)
# print(type(paises))

# Acessando elementos = Acessando via chave
print(paises['py'])
print(paises['br'])
# print(paises['ru']) #Caso chave não seja encontrada é retornado erro KeyError

# Acessando elementos = Acessando via get (RECOMENDADO) - Retorna None ao invés de KeyError
print(paises.get('br'))
print(paises.get('ru')) # Caso não encontre é retornado None

russia = paises.get('ru')
if russia:
    print("Encontrei o país")
else:
    print("Não encontrei o país")

pais = paises.get('ru')
if pais:
    print(f'Encontrei o país: {pais}')
else:
    print("Não encontrei o país")

# Define um valor caso não for encontrado a chave 'ru', retorna 'Não encontrado'

pais = paises.get('ru', 'Russia: Não encontrado')
print(pais) # Retornará "Russia: não encontrado"

# Procurar chave no dicionario - Não busca por valor de chave

print('br' in paises) # True
print('ru' in paises) # False
print('Estados Unidos' in paises) # False

if('ru' in paises):
    russia = paises['ru']
    print(russia)

# Aceita todos os tipos de dados
# Utilizando tupla como chave de dicionario. obs: recomendado pois a tupla é imutavel

localidades = {
    (35.6895, 39.6917): 'Escritório em Tóquio',
    (40.7128, 74.0060): 'Escritório em Nova Iórque',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario
# Forma 1 - Mais comum
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
receita['abr'] = 350 # Informando valor a ser adicionado
print(receita)

# Forma 1 - Utilizando com update()
novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# Atualizar dados em um dicionario
# Forma 1

receita['mai'] = 750
print(receita)

# Forma 2 - com update()

receita.update({'mar': 250})
print(receita)

# Conclusão: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# Em dicionarios NÃO podemos ter chaves repetidas

# Remover dados de um dicionario

# Forma 1 com pop('chave') - obrigatório informar a chave. KeyError se não encontrar a chave
receita.pop('mai')
print(receita)

# Forma 2 com pop('chave') retornando o valor da chave excluida
ret = receita.pop('abr')
print(ret) # Mostra o valor da chave excluida
print(receita)

# Forma 3 com del

del receita['fev'] # Retorna KeyError caso não encontrar a chave ['fev'] EXISTE neste exemplo, não retornará erro
print(receita)

# Imagine a seguinte situação em um comércio elêtronico, onde no carrinho de compras adicionamos.
"""
Carrinho de compras:
    Produto 1:
        - Nome:
        - Quantidade:
        - Preço:
    Produto 2:
        - Nome:
        - Quantidade:
        - Preço:   
"""

# Poderiamos utilizar uma lista para isso? SIM
# Teriamos que saber qual o indice de cada informação no produto 0 = Nome, 1 = Quantidade, 2 = Preço

carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Poderiamos utilizar uma tupla para isso? SIM
# Teriamos que saber qual o indice de cada informação no produto 0 = Nome, 1 = Quantidade, 2 = Preço

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)

# Poderiamos utilizar um dicionario para isso? SIM (Recomendado)
# Dessa forma facilmente adicionamos ou removemos produtos no carrinho e cada produto temos a informação do indice

carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'preço': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Métodos de dicionarios

d = dict(a=1, b=2, c=3)
print(d)

# Limpar o dicionario (zerar dados) utilizando clear()

d.clear()
print(d)

# Copiando um dicionario para outro utilizando copy()
# Forma 1 - Deep Copy
d = dict(a=1, b=2, c=3)
novo = d.copy() # Deep Copy
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Shallow Copy ( ao alterar o novo1, o d também é alterado )

d = dict(a=1, b=2, c=3)
print(d)
novo1 = d # Shallow Copy
novo1['d'] = 4
print(d)
print(novo1)

# Forma não usual de criação de dicionarios
# O metodo fromkeys() recebe dois parametros, um iteravel e um valor
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado

outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario) # Ira retornar {'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido', 'profile': 'desconhecido'}
print(type(usuario))

veja = {}.fromkeys('teste', 'valor')
print(veja) # Ira retornar {'t': 'valor', 'e': 'valor', 's': 'valor'} # Gerar chaves para cada letra sem repetição e atribui o valor (valor) para cada

veja = {}.fromkeys(range(1, 11), 'novo') # Ira retornar {1: 'novo', 2: 'novo', 3: 'novo', ...}
print(veja)

"""
Documentando funções com Docstring

OBS: Podemos ter acesso a documentacao de uma funcao em Python
utilizando a propriedade especial __doc__

Podemos utilizar a documentacao com a função help()
"""

# Exemplos


def diz_oi():
    """ Uma função simples que retorna a string 'Oi'"""
    return 'Oi! '


print(diz_oi.__doc__)

print(print.__doc__)


def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de numero ou o numero à potencia informada
    :param numero: Numero que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial, padrão igual a 2
    :return: Retorna o exponencial de numero a potencia
    """
    return numero ** potencia


print(exponencial.__doc__)

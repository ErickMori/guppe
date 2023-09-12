"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    -not, is
Oprerados binários:
    -and, or

Regras de funcionamento:
AND - Ambos os valores precisam ser True
OR - Um ou outro valor precisa ser True
NOT - O valor do booleano é invertido True == False, False == True
IS - O valor é comparado com um segundo valor
"""

ativo = True
logado = False

if ativo and logado:
    print("Bem vindo usuario")
else:
    print("Voce precisa ativar sua conta. Cheque seu email")

if ativo or logado:
    print("Bem vindo usuario")
else:
    print("Voce precisa ativar sua conta. Cheque seu email")

if not ativo:
    print("Voce precisa ativar sua conta. Cheque seu email")
else:
    print("Bem vindo usuario")

# possivel utilizar if ativo is not True:
if ativo is True:
    print("Bem vindo usuario")
else:
    print("Voce precisa ativar sua conta. Cheque seu email")
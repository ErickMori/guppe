"""
Estruturas condicionais
if, else, elif (else if)
"""

idade = 19
if idade < 18:
    print("Menor de idade")
    print(f'Idade: {idade}')
elif idade == 18:
    print("Tem 18 anos")
elif idade == 30:
    print("Tem 30 anos")
else:
    print("Maior de idade")
    print(f'Idade: {idade}')
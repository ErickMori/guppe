"""
Loop while

while expressão_booleana:
   //execução do loop enquanto expressão booleana for verdadeira

Expressão booleana é toda expressão onde o resultado é True ou False

"""
numero = 1
while numero <= 10:
    print(numero)
    numero = numero + 1

#Em um loop while é importante que cuidemos do critério de parada para não causar um loop infinito

resposta = ''
while resposta != 'sim' and resposta != 's':
    resposta = input("Já acabou Jéssica?")


#operações
operacao = int(input("Escolha um operação - digite o número \n 1 - Adição \n 2 - subtração \n 3 - divisão \n 4 - multiplicação "))
n1, n2 = map(int,input("Escolha dois números ").split())
if operacao == 1:
    operacao = n1 + n2
elif operacao == 2:
    operacao = n1 - n2
elif operacao == 3:
    operacao = n1 / n2
elif operacao == 4:
    operacao = n1*n2
par_impar = operacao % 2
if par_impar == 0:
    print("O resultado é par")
elif par_impar != 0:
    print("O resultado é impar")
if operacao < 0:
    print("É negativo")
elif operacao >= 0:
    print("É positivo")
decimal = operacao % 1
if decimal == 0:
    print("É inteiro")
elif decimal != 0:
    print("É decimal")

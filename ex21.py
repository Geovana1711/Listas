#caixa guloso
valor = int(input("Quantos você deseja sacar? "))
if valor < 10 or valor > 600:
    print("Quantia mínima ou máxima não permitida ")
else:
    nota100 = valor // 100
    valor = valor % 100
    notas50 = valor // 50
    valor = valor % 50
    notas10 = valor // 10
    valor = valor % 10
    notas5 = valor // 5
    valor = valor % 5
    notas1 = valor
print(f"Notas de 100 são {nota100}, notas de 50 são {notas50}, notas de 10 são {notas10}, notas de 5 são {notas5} e notas de são {notas1} ")

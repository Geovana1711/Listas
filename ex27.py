# 1. Entrada de dados (convertendo para float para aceitar kg quebrados)
kg_morango = float(input("Quantidade de morangos (kg): "))
kg_maca = float(input("Quantidade de maçãs (kg): "))

#Definição dos preços por quilo do Morango
if kg_morango <= 5:
    preco_unit_morango = 2.50
else:
    preco_unit_morango = 2.20

#Definição dos preços por quilo da Maçã
if kg_maca <= 5:
    preco_unit_maca = 1.80
else:
    preco_unit_maca = 1.50

#Cálculo dos valores brutos
total_morango = kg_morango * preco_unit_morango
total_maca = kg_maca * preco_unit_maca

valor_total = total_morango + total_maca
peso_total = kg_morango + kg_maca

if peso_total > 8 or valor_total > 25:
    valor_total = valor_total * 0.90 

#Saída do resultado
print(f"\nResumo da compra:")
print(f"Peso total: {peso_total} kg")
print(f"Valor a pagar: R$ {valor_total}")

#gasolina
litros, tipo =  input("Quantos litros o deseja? Deseja alcool ou gasolina ").split()
tipo = tipo.lower()
litros = float(litros)
desconto = 0
preco_alcool = litros * 2.5
preco_gasolina = litros * 1,9
if tipo == "alcool":
    if litros <= 20 :
        desconto = preco_alcool - preco_alcool*0.03
    elif litros > 20:
        desconto = preco_alcool - preco_alcool * 0.05
elif tipo == "gasolina":
    if litros <= 20:
        desconto = preco_gasolina - preco_gasolina*0.04
    elif litros > 20:
         desconto = preco_gasolina - preco_gasolina*0.06
print(f"A quantidade de litros foi {litros}, tipo {tipo}, valor total {desconto}")

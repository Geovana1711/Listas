valor = input("Escolha um número de 0 a 1000 ")
centena = int(valor[0])
dezena = int(valor[1])
unidade = int(valor[2])
plural = 0
centena_s,dezena_s,unidade_s  = "", "", "",
if centena > 1:
 centena_s = "s"
if dezena > 1:
  dezena_s = "s"
if unidade > 1:
  unidade_s = "s"

print(f"Valor de cada : {centena} centena{centena_s}, {dezena} dezena{dezena_s}, {unidade} unidade{unidade_s}")

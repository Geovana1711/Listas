print("Farei algumas perguntas e preciso que você responda com s para sim e n para não")
r1, r2, r3, r4, r5 = input("Telefonou para a vítima?\nEsteve no local do crime?\nMora perto da vítima? \nDevia para a vítima? \nJá trabalhou com a vítima \n  ").split()
resposta = [r1, r2, r3, r4, r5]
quantidade = resposta.count("s")
if quantidade == 2:
 print("É considerado suspeito")
elif quantidade == 3 or quantidade == 4:
 print("É cúmplice")
elif quantidade == 5:
 print("É o assassino")
else:
 print("Inocente")

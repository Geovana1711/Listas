n1, n2, n3 = map(int,input("Escreva as suas ultimas 3 notas ").split())
media = (n1+n2+n3)/3
if media == 10:
    print("Aprovado, com distinção")
elif media >= 7:
 print(f"Aprovado, com média {media}")
else:
    print(f"Reprovado, com média {media}")

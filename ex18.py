#Verificação de data
data = input("Digite a data atual no formato dd/mm/aaaa ")
partes = data.split("/")
if len(partes) != 3:  #tres respostas
    print("A data está errada, utilize no formado dd/mm/aaaa")
else:
    #Separação das variaveis por resposta -após .split
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])
    if dia < 1 or dia > 31:
        print("data está errada")
    elif mes == 2 and dia > 28:
        print("data está errada")
    elif mes > 12:
        print("data está errada")
    else :
        print("A data está correta")

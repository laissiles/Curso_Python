equipamento =[]
valor =[]
codigo=[] #[]= lista
resposta ="s"

while resposta =="s":
    equipamento.append((input("Equipamento: ")))
    valor.append(float(input("Valor: ")))
    codigo.append(int(input("Código: ")))
    resposta = input("Digite \"s\" para continuar: ")

for indice in range(0, len(equipamento)):
    print("\nEquipamento: ",(indice+1))
    print("Nome.......: ", equipamento[indice])
    print("Valor......: ", valor[indice])
    print("Código.....: ",codigo[indice])

#3- buscando elementos na lista
busca=input("\nDigite o nome quipamento que deseja buscar: ")
for indice in range(0,len(equipamento)):
    if busca==equipamento[indice]:
        print("Valor: ", valor[indice])
        print("Código: ", codigo[indice])


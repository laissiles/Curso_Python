#4- lista dentro de lista

inventario=[]
resposta = "S"
while resposta == "S":
    equipamento=[input("Equipamento: "), #0
                 float(input("Valor: ")), #1
                 int(input("Número Serial: ")),#2
                 input("Departamento: ")]#3
    inventario.append(equipamento)
    resposta = input("Digite \"S\"para continuar: ").upper()

#### mostra os itens
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

#### busca itens
busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("Valor..: ", elemento[1])
        print("Serial.:", elemento[2])

#### item a ser depreciado
depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("Valor antigo: ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo valor: ", elemento[1])

#### deletar um item
serial=int(input("\nDigite o serial do equipamento que será excluído: "))
for elemento in inventario:
    if elemento[2]==serial:
        inventario.remove(elemento)

#### mostra os itens
for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.:", elemento[3])

#### dados sobre os equipamentos
valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))

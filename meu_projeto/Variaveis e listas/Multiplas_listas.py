#depreciacao e exclusão

inventario = []
resposta = "S"
while resposta == "S":
    equipamento=[input("Equipamento: "),
                float(input("Valor: ")),
                int(input("Nº serial: ")),
                input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite S para continuar o cadastro").upper()

for elemento in inventario:
    print("Nome............",elemento[0])
    print("Valor..........", elemento[1])
    print("Serial.........", elemento[2])
    print("Departamento...", elemento[3])

busca = input("\nDigite o nome do elemento que deseja buscar:")
for elemento in inventario:
    if busca == elemento[0]:
        print("Valor......", elemento[1])
        print("Nº serial...", elemento[2])


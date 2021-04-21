#listas multiplas
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Nº serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar com o cadastro: ").upper()


busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print ("Valor: ", valores[indice])
        print ("Serial: ", seriais[indice])
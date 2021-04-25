def preenche_inventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento=[input("Equipamento: "),
                    float(input("Valor: ")),
                    int(input("Nº serial: ")),
                    input("Departamento: ")]
        lista.append(equipamento)
        resposta = input("Digite S para continuar o cadastro: \n").upper()


def imprimir_elementos(lista):
    for elemento in lista:
        print("Nome............",elemento[0])
        print("Valor..........", elemento[1])
        print("Serial.........", elemento[2])
        print("Departamento...", elemento[3])
        print("-------------------------------")

        

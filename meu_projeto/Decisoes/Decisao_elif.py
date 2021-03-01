nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
esta_com_pais= input("esta com seus pais?").upper()

if idade >=18: #se for maior ou igual q 18 imprimie
    print("Parabéns "+nome+ " vc já é maior de idade")
elif esta_com_pais=="SIM": #se a primeira condição falhar e essa passar, imprime essa
    print("então pode entrar")
else: #se as duas de cima falhar imprime essa
    print("Olá "+nome+ " vc ainda não é maior de idade!")


    
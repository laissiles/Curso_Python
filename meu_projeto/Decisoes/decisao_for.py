tabuada = int(input("Digite um numero para exibir a tabuada: "))
print ("tabuada do numero: ", tabuada)
for valor in range(0,11,1):
    print(str(tabuada) + " x " + str(valor) + " = "+ str((tabuada*valor))) #IDENTAÇÃO É IMPORTANTE

    #in range(1,11,1): =  dentro da faixa (1- inicio do laço. 11- o fim, 1 incremento, pois vamos começar com a multiplicação
    # do 1, e vai no maximo a 10, incrementando de 1 em 1
    # ex- se eu quiser mostrar a tabuada até o 20,=  in range(1,21,1):


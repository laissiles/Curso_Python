#exemplo de um inventario - lista simples


inventario =[] #Lista, vetor
resposta ="s"

while resposta == "s":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Código: ")))
    resposta=input("Digite \"s\" para continuar: ") #para imprimir "s" com as aspas

#print(str (inventario)) - imprime todos os dados da lista
#print(str (inventario[1])) #imprime o item 1 (da lista)- vetor inicia em 0

for elemento in inventario: #imprime a lista de forma "organizada - e o cont? elemento =0, e o limite é o tam de inventario
    print(elemento)
#inventario.append =
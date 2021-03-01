nome = input("Digite um funcionario: ")
empresa = input ("Digite a instituição: ")
qta_funcionarios = int(input("digite a quantidade de funcionarios: "))
mediaSalarial = float(input("Digite a média do salário: "))

print(nome + " trabalha na empresa " + empresa) # string com string
print ("e possui", qta_funcionarios, "funcionarios") #string com int
print ("e a media de salario é de: "+str(mediaSalarial)) #string com float

print ("Para ver o tipo de variavel usamos type: ", type(nome))
print ("Para ver o tipo de variavel usamos type: ", type(qta_funcionarios))
print ("Para ver o tipo de variavel usamos type: ", type(mediaSalarial))
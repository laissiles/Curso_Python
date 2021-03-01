numero = int(input("Digite um numero: "))

while numero<100: #enquanto o numero for menor que 10, ele mostra os numeros e soma 1: ex 10 (11, 12, 12...99)
    print("\t"+ str(numero)) #//t - tabulação a esquerda/// str é para "transformar" o numero em string na impressão
    numero=numero+1

print("Fim do laço")
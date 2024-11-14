
numero = int (input("Digite um numero para ser calculado o fatorial:"))#pede pro usuario digitar um numero
contador = numero
nulo = 1
while contador > 0: #cria um laço de repetição verificando se a variavel é maior que 0
    print ("{}".format(contador), end ="")
    print (" x " if contador >1 else " = ", end="")# exibe se o contador é maior que 1 
    nulo *=contador# multiplica a variavel nulo vezes o contador
    contador -= 1# contador fica igual a -1
print (f"{nulo}")#exibe o resultado
#pede para o usuario inserir um numero
tabuada = int (input("Digite um numero para a tabuada:"))
#percorre o numero escolhido de 1 a 10
for count in range(10):
        print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
        #exibe a tabuada na qual o numero foi escolhido
        

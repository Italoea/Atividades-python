numero = int (input("Digite um número:"))

#percorre de 1 ao numero que foi escrito
for contador in range (1, numero +1):
    #verifica se o resto da divisão é 0
    if numero % contador ==0:
        #mostra na tela
        print (f"{contador}", end= " ")

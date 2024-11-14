#pede para inserir os numeros
n1 = int (input("Digite um número:"))
n2 = int (input("Digite um número:"))
n3 = int (input("Digite um número:"))
n4 = int (input("Digite um número:"))
#cria uma função para esses numeros
def media (n1,n2,n3,n4):
    #cria uma variavel para a soma e a divisão dos numeros
    total = (n1+n2+n3+n4)/4
    #retorna a variavel total
    return total
#exibe a média
print ("A média do aluno é:", media (n1,n2,n3,n4))
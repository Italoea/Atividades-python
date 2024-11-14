#cria a função 
def contar_vogais(string):
    string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
    vogais = 'aeiou' #exibe as vogais
    return sum(string.count(i) for i in vogais) #Percorre toda a palavra

#exibe quantas vogais tem
print(contar_vogais("seja bem vindo"))
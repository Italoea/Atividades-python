import random #importei a bibliotecal
numero_aleatorio = random.randint(0, 10)# pedi que os numeros só fossem de 0 á 10

while True:#Criei um laço de repetição
    numero = int (input ("Digite Um numero:"))# criei uma variavel 
    if numero< numero_aleatorio: #verfifica se o numero foi a menos
        print("Está frio tente um número maior")

    if numero> numero_aleatorio:
        print ("Está quente tente um numero menor")#verfifica se o numero foi a mais
    elif numero_aleatorio== numero:
        print ("Parabéns vc acertou o numero!!!!!!!")#mostra que você acertou o numero
        break# para o prigrama

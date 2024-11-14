import random
numero_aleatorio = random.randint(0, 101)

while True:
    numero = int (input ("Digite Um numero:"))
    if numero< numero_aleatorio:
        print("Esttá frio tente um número maior")

    if numero> numero_aleatorio:
        print ("Está quente tente um numero menor")
    elif numero_aleatorio== numero:
        print ("Parabéns vc acertou o numero!!!!!!!")
        break

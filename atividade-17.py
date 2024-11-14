from random import randint
import random

# Definimos o que a nossa senha irá conter
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbolos = ['!', '@', '#', '$', '%', '&', '*']

def passwords(level: int):
    senha = ''

    # Testamos qual nível foi escolhido
    # Quanto mais alto o nível, mais coisas incrementamos na senha
    if level == 0:
        for i in range(4):
            senha += random.choice(letras)
        for i in range(1):
           senha += str(random.choice(num))

    elif level == 1:
        for i in range(5):
            n_random = randint(0, 9)
            senha += random.choice(letras)
            senha += str(random.choice(num)) if n_random % 2 == 0 else random.choice(simbolos)

    elif level == 2:
        for i in range(8):
            n_random = randint(0, 9)
            senha += random.choice(letras) if n_random % 2 == 0 else str(random.choice(letras)).upper()
            n_random = randint(0, 9)
            senha += str(random.choice(num)) if n_random % 2 == 0 else random.choice(simbolos)

    return senha
while True:
    print("Qual o tipo de senha que você quer gerar ?")
    level = input("[0] - Fraca\n[1] - Média\n[2] - Forte\n: ")

    while not level.isnumeric() or (int(level) < 0 or int(level) > 2): # Verifica se foi digitado o nivel, corretamente
        print("O tipo tem de ser um número!!!\n")
        print("Qual o tipo de senha que você quer gerar ?")
        level = input("[0] - Fraca\n[1] - Média\n[2] - Forte\n: ")

    level = int(level)
    print(passwords(level))
from random import randint
import time

numero = False

print("Vamos jogar dados ?")

while not numero:
    vezes = input("Digite quantas vezes vocaê quer jogar o dado: ")

    while not str(vezes).isnumeric() or int(vezes) < 1: # Verifica se foi digitado o numero certo
        print("\nPrecisa ser um número e maior do que um !!!\n")
        vezes1 = input("Digite quantas vezes pretende jogar o dado: ")

    vezes1 = int (vezes)

    for i in range(vezes):
        print("Jogando dado...")
        time.sleep(1)
        print(f"Na jogada {i+1} o número foi {randint(1,6)}") # envia um numero aleatorio de 1 á 6

    print("\nQuer jogar de novo?\n[1] - Sim\nQualquer outra tecla para sair.")
    esc_jog = input()

    end = True if not esc_jog == "1" else False
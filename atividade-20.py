with open('lista.txt', 'r') as lista: # Abrimos, lemos o arquivos e fechamos de forma automática
    identificar = lista.read()

total = 0

identificar = identificar.split(" ")

for numero in identificar:
    num = numero.strip()
    total += int(num) # Soma o número que foi testado.

print ( f"\n A média foi de: {"%.2f" % (total/len(identificar))}")
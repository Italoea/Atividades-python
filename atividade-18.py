
import random

def lancar_dado_simples(n):
    resultados = [random.randint(1, 6) for _ in range(n)]
    frequencias = {face: resultados.count(face) for face in range(1, 7)}
    return frequencias


n = int(input("Quantas vezes você deseja lançar o dado? "))
frequencias = lancar_dado_simples(n)
print("Frequências de cada face:", frequencias)


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        
    def apresentar(self):
        print (f"Prazer eu sou o {self.nome}")

aluno = Aluno ("Ítalo")
aluno.apresentar()
       
        
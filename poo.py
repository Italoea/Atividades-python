class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def mostrar_dimensoes(self):
        print(f"Largura: {self.largura}, Altura: {self.altura}")


retangulo = Retangulo(5, 3)
retangulo.mostrar_dimensoes()
print("Área:", retangulo.area())
print("Perímetro:", retangulo.perimetro())

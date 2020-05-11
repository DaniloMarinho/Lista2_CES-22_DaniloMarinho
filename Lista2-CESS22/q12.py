class Veiculo:
    def descricao(self):
        print("Veiculo")

class Carro(Veiculo):
    def descricao(self):
        print("Carro")

V = Veiculo()
V.descricao()
C = Carro()
C.descricao()
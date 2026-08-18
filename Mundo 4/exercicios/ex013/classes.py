class Mae:
    def __init__(self, nome):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM com leite condensado")

    def fazer_coxinha(self):
        print(f"{self.nome} faz coxinha com óleo de soja")

class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM com leite em pó")

class Filho(Mae):
    def fazer_coxinha(self):
        print(f"{self.nome} faz COXINHA com óleo vegetal")
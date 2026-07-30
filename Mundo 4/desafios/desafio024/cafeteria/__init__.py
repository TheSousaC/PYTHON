from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print("-- Preparando O Pedido --")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("-- Bebida Pronta --")

    def ferver_agua(self):
        print("Fervendo a água a 100°C.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        print("Passando a água pressurizada pelo pó de café moído.")

    def servir(self):
        print("Servindo em xicará pequena.")

class Cha(BebidaQuente):
    def misturar(self):
        print("Mergulhando o sachê em ervas amargas.")

    def servir(self):
        print("Servindo na Caneca de porcelana com limão.")

class Leite(BebidaQuente):
    def misturar(self):
        print("Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("Servindo em uma caneca grande, já com café")
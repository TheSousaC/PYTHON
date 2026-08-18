from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass
class Pato(Animal):
    def emitir_som(self):
        print("QUAK QUACK")

class Cachorro(Animal):
    def emitir_som(self):
        print("AU AU AU AU AU")

class Splitz(Cachorro):
    def emitir_som(self):
        print("AU AU AU AU AU (com classe)")

class PitBull(Cachorro):
    def emitir_som(self):
        print("AU AU AU AU (com raiva)")

class Gato(Animal):
    def emitir_som(self):
        print("MINHAUUUUUUUUUUUUUUUUUUUUU")

class Galinha(Animal):
    def emitir_som(self):
        print("CÓ CÓ CÓ CÓ CÓ")
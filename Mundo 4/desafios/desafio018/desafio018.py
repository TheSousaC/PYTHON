##Classe Churrasco
from rich.panel import Panel
from rich import print

class Churrasco:
    ##Atributos de Classe
    consumo_pes:float = 0.400 ##Cada pessoa vai comer em média 400g
    precoKg:float = 82.40 ##O preço de cada quilo de carne

    ##Metodo e atributos de Instância
    def __init__(self, nome, qnt):
        self.nome = nome
        self.qnt = qnt

    def calcular_qnt_carne(self) -> float:
        return self.qnt * Churrasco.consumo_pes

    def calcular_preco_total(self) -> float:
        return Churrasco.precoKg * self.calcular_qnt_carne()

    def calcular_custo_individual(self) -> float:
        return self.calcular_preco_total() / self.qnt

    def analisar(self):
        conteudo = f'Analisando o {self.nome} com {self.qnt} convidados'
        conteudo += f"\nCada Participante comerá {Churrasco.consumo_pes}Kg e cada Kg custa R${Churrasco.precoKg:,.2f}"
        conteudo += f"\nRecomendo comprar {self.calcular_qnt_carne():.3f}Kg de carne"
        conteudo += f"\nO custo total será de R${self.calcular_preco_total():,.2f}"
        conteudo += f'\nCada pessoa pagará R${self.calcular_custo_individual():,.2f}'
        painel = Panel(conteudo, title=self.nome)
        print(painel)


chu = Churrasco("Chuchu", 60)
chu.analisar()

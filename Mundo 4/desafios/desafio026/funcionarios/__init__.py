from abc import ABC, abstractmethod
from rich import inspect ,print
from rich.panel import Panel
class Funcionario(ABC):

    sal_minimo = 1612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        correspondencia = self.salario / Funcionario.sal_minimo
        conteudo = f"O salário de {self.nome} é de R${self.salario:.2f} e corresponde a {correspondencia:.1f} salários minimos"
        painel = Panel(conteudo, title="Análise de Salário", width=40)
        print(painel)


class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trabalhadas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas
        self.sal_bruto = self.valor_hora * self.horas_trabalhadas

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss/ 100)

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto = Funcionario.sal_minimo):
        super().__init__(nome)
        self.nome = nome
        self.salario_bruto = salario_bruto

    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * self.inss/ 100)

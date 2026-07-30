from abc import ABC, abstractmethod
from rich import inspect ,print
from rich.panel import Panel
class Funcionario(ABC):

    sal_minimo = 1612
    inss = 7.5

    def __init__(self, nome, sal_bruto, salario):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        correspondencia = self.sal_bruto/Funcionario.sal_minimo
        conteudo = f"O salário de {self.nome} é de {self.calcular_salario():.2f} e corresponde a {correspondencia:.1f} salários minimos"
        painel = Panel(conteudo, title="Análise de Salário", width=40)
        print(painel)


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome, 0,0)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario(self):
        salario = self.valor_hora * self.horas_trabalhadas
        salario = salario - (salario * self.inss)/100
        salario = round(salario, 2)
        return salario

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto, salario = 0):
        super().__init__(nome, salario_bruto, salario)
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = salario

    def calcular_salario(self):
        salario = self.salario_bruto - (self.salario * self.inss)/100
        salario = round(salario, 2)
        return salario

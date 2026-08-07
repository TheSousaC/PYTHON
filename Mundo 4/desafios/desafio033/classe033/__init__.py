from abc import ABC
from datetime import datetime
from rich import print, inspect


class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento
        self._idade = datetime.now().year - self._nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        atual = datetime.today().year
        if nascimento > atual or nascimento < 1940:
            print("Ano invalido")
        else:
            self._nascimento = nascimento

    @property
    def idade(self):
        return datetime.now().year - self._nascimento

    @idade.setter
    def idade(self, idade):
        raise PermissionError("Você não pode mudar a idade, mude o ano de nascimento")


class Aluno(Pessoa):

    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self.curso_aluno = curso

    @property
    def curso(self):
        return self.curso_aluno

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self.curso_aluno = curso
        else:
            print("Curso invalido")

    def add_curso(self, curso):
        if 3 < len(curso) < 5:
            Aluno.cursos_oficiais.append(curso)
            # self.curso_aluno = curso




from abc import ABC, abstractmethod

class Pessoa(ABC): ##Agr essa classe abstrata tem uma classe mae: ABC
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O {self.nome} fez matricula!")

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso}")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O Profº {self.nome} acabou de iniciar a Aula!")

    def estudar(self):
        print(f"{self.nome} está aumentando seu nivel em {self.especialidade}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto!")

    def estudar(self):
        print(f"{self.nome} está estudando {self.setor}")
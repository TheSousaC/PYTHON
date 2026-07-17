from rich import inspect, print

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O {self.nome} fez matricula!")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O Profº {self.nome} acabou de iniciar a Aula!")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto!")


a1 = Aluno("Gustavo", 4, "Maternal II", "A1")
a1.fazer_aniversario()
a1.fazer_matricula()
# inspect(a1)
p1 = Professor("Dani C.", 22, "Infantil", "II")
p1.fazer_aniversario()
p1.dar_aula()
# inspect(p1)
f1 = Funcionario("Julio", 18, "Plantador de Batata", "Agricultor")
f1.fazer_aniversario()
f1.bater_ponto()
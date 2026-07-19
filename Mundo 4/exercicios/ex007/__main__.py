from rich import inspect, print
from classes import Pessoa, Aluno, Professor, Funcionario
def main():
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

    a1.estudar()
    p1. estudar()
    f1.estudar()


if __name__ == "__main__":
    main()
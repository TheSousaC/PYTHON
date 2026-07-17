from rich import inspect, print
from classesEx005 import Aluno, Professor, Funcionario

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

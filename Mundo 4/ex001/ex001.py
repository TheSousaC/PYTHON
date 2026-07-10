##Criando minha Classe

class Aluno:
    def __init__(self):  ##Metodo Construtor
        ##Atributos de Instância
        self.nome = ""
        self.idade = 0

    ##Metodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagemTOP(self):
        return f"O(a) {self.nome} tem {self.idade} anos e é um aluno nota 10!!!"


##Declaralção de Objetos
aluno1 = Aluno()  ## O "()" é o metodo construtor que declara/instância a Classe
## aluno1 é um objeto
aluno1.nome = str(input("Digite o nome do aluno: "))
aluno1.idade = int(input("Digite sua idade: "))
print(aluno1.mensagemTOP())

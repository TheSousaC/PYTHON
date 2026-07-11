##Melhorando a Minha Classe do Ex001

class Aluno:
    """
    A Classe Aluno cria um aluno que tem Nome e idade

    Para criar/cadastrar um aluno você precisa:
    variavel = Aluno(nome, idade)
    """

    def __init__(self, nome="Aluno", idade=4):  ##Metodo Construtor
        ##Atributos de Instância
        self.nome = nome
        self.idade = idade

    ##     atributo    parametro da instancia

    ##Metodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):  ##Dunder Method -> Metodo de mostrar uma mensagem pro objeto
        return f"O(a) {self.nome} tem {self.idade} anos e é um aluno nota 10!!!"


##Declaralção de Objetos
aluno1 = Aluno("Gabriel", 18)  ## O "()" é o metodo construtor que declara/instância a Classe
## aluno1 é um objeto
# print(aluno1)

aluno2 = Aluno("Gustavo Yamada", 5)  ##O aluno2 é outro objeto qu já vem com dois parametros preenchidos
# print(aluno2)

# print(Aluno.__doc__) ##Docstring -> Metodo de mostrar a doc da Classe

print(aluno1.__dict__) ##Mostra o Dicionário \\ Atributo
print(aluno2.__getstate__()) ##Metodo
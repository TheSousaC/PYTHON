from Exercicios.ex115.menu import menu
from Exercicios.ex115.cadastrar import cadastrar
from Exercicios.ex115.Ler import lerArquivo

def opcao(msg):
    while True:
        menu()
        numero = str(input(msg))
        try:
            select = int(numero)
            if select == 1:
                lerArquivo()
            elif select == 2:
                cadastrar()
            elif select == 3:
                break
            else:
                print("Opção não existe")
        except ValueError:
            print("Erro ao digitar o valor. Por Favor digite um valor válido")
        except TypeError:
            print("Tipo do valor invalido")
        finally:
            print("Volte sempre!")

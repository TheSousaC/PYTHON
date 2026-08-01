from ex010 import *

def main():
    av1 = Avaliacao("Gabriel", "Física", 8)
    av1.nota = 10
    print(f"{av1.nome} tirou {av1.nota} em {av1.diciplina}")
if __name__ == "__main__":
    main()
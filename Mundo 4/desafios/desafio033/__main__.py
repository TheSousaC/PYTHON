from classe033 import *

def main():
    a1 = Aluno("Gabriel", 2007, "ADS")
    a1.add_curso("PWE")
    # a1.curso = "PWE"
    print(a1.idade)

    inspect(a1, private=True, methods=True)

if __name__ == "__main__":
    main()
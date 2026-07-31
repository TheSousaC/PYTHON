from personagens import *


def main():
    p1 = Guerreiro("Thor", 5000)
    p2 = Mago("Dani", 3000)
    p1.atacar(p2, 300)
    p2.atacar(p1, 300)
    p2.curar()
    p1.curar()
    p2.atacar(p1, 1000)
    p1.atacar(p2, 1000)


if __name__ == '__main__':
    main()

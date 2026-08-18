from classes import *

def main():
    mamis = Mae("Denilda")
    mamis.fazer_pudim()
    mamis.fazer_coxinha()

    roberto = Filho("Roberto")
    roberto.fazer_coxinha()
    roberto.fazer_pudim()

    renata = Filha("Renata")
    renata.fazer_coxinha()
    renata.fazer_pudim()

if __name__ == "__main__":
    main()
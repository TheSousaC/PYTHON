from ex008 import *

def main():
    conta1 = TheBank(7405, "Gabriel Costa", 1000)
    conta1.despositar(1500)
    conta1.sacar(2_000_000_222)
    print(conta1)

if __name__ == "__main__":
    main()
from classe031 import *

def main():
    re = Retangulo(10, 30)
    try:
        re.medidas = (100,200)
        print(re.area)
        inspect(re, private=True, methods=True)
    except Exception as e:
        print(f"Ocorreu um erro {e} do tipo: {type(e)}")

if __name__ == "__main__":
    main()
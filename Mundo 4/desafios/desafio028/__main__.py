from email._header_value_parser import Terminal

from classe028 import *

def main():
    t = Termostato()
    try:
        t.temperatura = 22.2
        print(f"A tempertura atual é {t.ftemperatura}")
    except Exception as erro:
        print(f"Houve um erro de: {erro}")
if __name__ == '__main__':
    main()
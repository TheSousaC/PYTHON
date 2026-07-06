##Interactive Help com cores
cores = (
    "\033[m",  ##Nada
    "\033[0;30;41m",  ##Vermelho
    "\033[0;30;42m",
)


def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 1)
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')


comando = ""
while True:
    titulo("Sistema HELPER", 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "fim":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO", 1)

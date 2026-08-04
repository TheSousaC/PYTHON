import hashlib
from rich import print, inspect

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha):
        try:
            __hash_senha = hashlib.sha256(str(senha).encode()).hexdigest()
            self.__hash = __hash_senha
        except Exception as e:
            print(f"[red] Erro ao criptografar a senha em sha256:[/] {e}")


    def validar(self,senha):
        try:
            cript = hashlib.sha256(str(cript).encode()).hexdigest()
            if cript != self.__hash:
                print("[red] Senha invalida![/]")
            else:
                print("[green] Senha validada![/]")

        except Exception as e:
            print(f"[red]Erro na validação da senha:[/] {e}")
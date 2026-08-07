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
        if len(senha) > 8:
            hash_senha = hashlib.sha256(str(senha).encode().strip()).hexdigest()
            self.__hash = hash_senha
        else:
            raise PermissionError("Senha com menos de 8 caracteres")

    def validar(self, senha):
        try:
            cript = hashlib.sha256(str(senha).encode()).hexdigest()
            if cript != self.__hash:
                print("[red] Senha invalida![/]")
            else:
                print("[green] Senha validada![/]")

        except Exception as e:
            print(f"[red]Erro na validação da senha:[/] {e}")

##Abrir um site
from asyncio import timeout

import requests

try:
    site = requests.get('https://crashware.onrender.com/', timeout=10)
    # if timeout < 5:
    #     print("Aguarde...")
    #     for c in range(0, timeout):
    #         print(c, end=" ")
    print("O site está acessivel!")
except:
    print("O site não está acessivel!")



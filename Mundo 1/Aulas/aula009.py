# Cadeias de Texto

#Fatiamento
Frase = "Eu amo risole"
Frase[2]
# ele pegará o U

Frase[2:5]
# Ele pegará "u am" o "O" nao é pego
# Se eu fizer Frase[2:9] ele pega "u amo risole" mesmo nao existindo o 9

Frase[:5]
# vai do inicio até o 5


#USAR
#O .find
Frase.find("amo")

Frase.replace("risole", "Salgado")

#upper() deixa td maiusculo
#lower() deixa td minusculo
#capitalize() só o primeiro vai ser maiusculo
#title() vai analizar quantas palavras tem
#strip() vai remover todos os espaços inuteis da frase
#rstrip() vai remover somente os espaços inuteis do final
#lstrip() vai remover somente os espaços inuteis do começo
#slipt() divide a frase e cada palavra vira uma nova lista
# '-'.join(Frase) juntará as letras sem espaço usando o -
#'-'.join(Frase.split()) juntará as palavras usando -
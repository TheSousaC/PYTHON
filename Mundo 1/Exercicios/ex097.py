##Função escreva()

def escreva(txt):
    tam = len(txt) + 4
    print("=" * tam)
    print(f"{txt}".center(tam))
    print("=" * tam)


escreva("Gabriel Top")
escreva("Serelepe")
escreva("Hoje está muito frio")
escreva("Oi")

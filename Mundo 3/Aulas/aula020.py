##Funçoes (def)
# def titulo(txt):
#     print("="*30)
#     print(txt)
#     print("="*30)
#
# titulo("Gabriel é lindo")
# titulo("Eu to com frio")
# titulo("Lua")

# def contador(*num):
#     tam = len(num)
#     print(f"Recebi os valores {num} e ao todo são: {tam} números ")
#
# contador(1, 2, 3, 4)
# contador(2, 6, 7)

def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 100, 50, 40, 67, 47, 74, 7, 4, 28, 10]
dobrar(valores)
print(valores)
print(len(valores))

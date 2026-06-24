## imapres de 1 a 500 e que sao multiplos de 3

s = 0
quant = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        quant = quant + 1
        s += c
print(f"Os números imapares de 1 a 500 e divisiveis por 3  são: {quant} e somados são: {s}")
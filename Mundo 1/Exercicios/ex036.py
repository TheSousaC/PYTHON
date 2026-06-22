## Financiamento de uma casa

valorImovel = float(input('Qual o valor do Imovel? R$'))
salario = float(input("Digite seu salário: R$"))
anos = float(input("Quantos anos deseja pagar: "))

meses = anos * 12
minimo = (salario * 30) / 100
prestacao = valorImovel / meses

if prestacao <= minimo:
    print("Financiamento Aprovado!")
    print(f"Você pagará R${prestacao:.2f} em {meses} meses. Pois as parcelas nao passam de 30% de seu salário que é {minimo:.3f}.")
else:
    print("Financiamento Negado")
    print(f"Você não pode financiar, pois as parcelas exedem 30% de seu salário que é {minimo:.3f}")
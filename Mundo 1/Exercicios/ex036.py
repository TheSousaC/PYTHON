## Financiamento de uma casa

valorImovel = float(input('Qual o valor do Imovel? R$'))
salarioComprador = float(input("Digite seu salário: R$"))
Anos_parcelas = float(input("Quantos anos deseja pagar: "))


minimoSalario = salarioComprador * 0.30
meses = Anos_parcelas / 12

valorParcelas = valorImovel / meses

if valorParcelas <= minimoSalario:
    print("Financiamento Aprovado!")
    print(f"Você pagará R${valorParcelas:.2f} em {Anos_parcelas} anos. Pois as parcelas nao passam de 30% de seu salário")
else:
    print("Financiamento Negado")
    print("Você não pode financiar, pois as parcelas exedem 30% de seu salário")
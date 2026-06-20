## Salario e aumento

nome_Funcionario = str(input('Qual o nome do funcionario? '))
salario_Funcionario = float(input(f"Qual o salário do(a) {nome_Funcionario}? "))

if salario_Funcionario <= 1250:
    novo = salario_Funcionario + (salario_Funcionario * 15) /100
    print(f"O salário de {nome_Funcionario} recebeu um aumento de 15%, e agorá é de R${novo:.2f}")
else:
    novo = salario_Funcionario + (salario_Funcionario * 10) /100
    print(f"O salário de {nome_Funcionario} recebeu um aumento de 10%, e agora é de R${novo:.2f}")
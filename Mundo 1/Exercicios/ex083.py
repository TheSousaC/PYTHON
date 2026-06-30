##Verificar se tem () completas

expressao = []
num = str(input("Digite uma expressão matemática: "))
expressao.append(num)
if len(expressao[0]) == "(" and len(expressao[0]) == ")":
    print("Expressão correta")
elif len(expressao[0]) == "(" and len(expressao[0]) != ")" or len(expressao[0]) != "(" and len(expressao[0]) != ")":
    print("Expressaão errada")

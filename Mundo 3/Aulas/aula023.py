## Try & Exception

try:
    a = int(input('Digite um valor: '))
    b = int(input('Digite um valor: '))
    r = a / b
except (ValueError, TypeError):
    print('Valor incorreto ou o Tipo incorreto!')
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')
except KeyboardInterrupt:
    print("O usuario parou o programa!")
except Exception as erro:
    print(f'Ocorreu um erro na entrada {erro}')
else:
    print(f"O resultado é {r}")
finally:
    print("Volte sempre. Mt obg!!")

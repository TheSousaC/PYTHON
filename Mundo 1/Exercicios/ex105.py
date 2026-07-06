##Função Notas

def notas(*n, sit=False):
    """
    -> Função para analisar as notas e condições de uma turma
    :param n: Uma ou mais notas dos alunos (Aceita variáveis)
    :param sit: (Opcional) Verificará a média e retorna a situação da turma
    :return: Retorna a lista de notas
    """
    turma = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'media': sum(n) / len(n),
    }
    if sit:
        if turma['media'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['media'] >= 5 and turma['media'] < 7:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'

    return turma


resp = notas(10, 0.5, 1, 4, 5, 3, 5, 7, sit=True)
print(resp)
help(notas)

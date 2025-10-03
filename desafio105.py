#Exercício Python 105: Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e vai retornar um dicionário 
# com as seguintes informações:

#    Quantidade de notas
#    A maior nota
#    A menor nota
#    A média da turma
#    A situação (opcional)


#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.



def notas(*num, sit=False):
    """Função para analisar notas e situações de valunos

    Args:
        :param m: uma ou mais notas dos alunos (aceita várias)
        :param sit: Valor opcional, indicando se deve ou não adicionar a situação
        
    Returns:
        Dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r["total"] = len(num)
    r["maior"] = max(num)
    r["menor"] = min(num)
    r["média"] = sum(num)/len(num)
    if sit:
        if r["média"] < 6:
            r["situação"] = "Ruim"
        elif r["média"] <= 7:
            r["situação"] = "Boa"
        else:
            r["situação"] = "Otima"
    return r

resp = notas(5.5, 5, 10, 8.5, sit = True)
print(resp)
#help(notas)

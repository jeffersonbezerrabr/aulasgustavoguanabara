# Exercício Python 102: Crie um programa que tenha uma 
# função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado 
# ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """_summary_

    Args:
        num (int, optional): _description_. Defaults to 1.
        show (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(" = ", end='')
        f *= c
    return f

print(fatorial(5, True))
    
"""
Funções (def) em Python - *args **kwargs
"""

def func(*args, **kwargs):
    print(args)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

list = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
func(*list, *list2, nome='Vilson', sobrenome='Lopes', idade=36)

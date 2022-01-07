# Relacionar as duas listas usando enumerate()
vendedores = ['Marcus', 'Amanda', 'Ale', 'Carol']
vendas = [15, 20, 10, 30]


for i, vendedor in enumerate(vendedores):
    print(f'Vendedor(a): {vendedor} - {vendas[i]} vendas.')

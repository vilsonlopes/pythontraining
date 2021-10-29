def calcula_pagamento(qtd_horas, valor_horas):
    horas = float(qtd_horas)
    valor = float(valor_horas)

    if horas <= 40:
        salario = horas * valor
    else:
        hora_excedida = horas - 40
        salario = 40 * valor + (hora_excedida * (1.5 * valor))

    return salario

str_horas = input('Digite as horas trabalhadas: ')
str_valor = input('Digite o valor pago por hora: ')
salario_total = calcula_pagamento(str_horas, str_valor)

print(f'Seu pagamento será de R$-{salario_total}.')

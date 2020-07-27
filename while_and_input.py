altura = float(input('Qual sua altura em CM? '))
if altura >= 36:
    print('\nVocê é alto o suficiente.')
else:
    print('\nVocê poderá andar quando estiver mais velho.')

# Usando uma flag

prompt = '\nDiga-me uma coisa e vou repetir de volta para você: '
prompt += '\nDigite "quit" para terminar o programa. '
ativo = True
while ativo:
    message = input(prompt)
    if message == 'quit':
        ativo = False
    else:
        print(message)

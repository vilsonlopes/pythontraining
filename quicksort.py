# # Função para somar os números inteiros de uma lista
# def soma(lista):
#     total = 0
#     for x in lista:
#         total += x
#     return total
#
#
# print(soma([20, 2, 3, 4]))

#
# # Função para contar quantos elementos há em uma lista
# def contador(lista):
#     total = 0
#     for x in (lista):
#         total += 1
#     return total
#
#
# print(contador([0, 1, 2, 3, 4, 3, 6, 9, 10, 90, 'Vilson']))


# # Função para encontrar maior número em uma lista
# def valorMaisAlto(lista):
#     alto = lista[0]
#     for i in (lista):
#         if i > alto:
#             alto = i
#
#     return alto
#
#
# print(valorMaisAlto([5, 2, 99, 20, 35, 1]))


# def quicksort(array):
#     if len(array) < 2:
#         return array
#     if len(array) == 2 and array[0] < array[1]:
#         return array
#     if len(array) == 2 and array[0] > array[1]:
#         array.reverse()
#         return array
#     if len(array) > 2:
#         return 'Esse código é para dois numeros apenas.'
#
#
# print(quicksort([7, 6]))


# Código de ordenação quicksort
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        #return quicksort(menores) + [pivo] + quicksort(maiores)
        print(array)
        print(quicksort(menores))
        print(pivo)
        print(maiores)


print(quicksort([3, 5, 2, 1, 4]))

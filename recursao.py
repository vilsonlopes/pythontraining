# def regressiva(i):
#     print(i)
#     if i <= 1:
#         return
#     else:
#         return regressiva(i - 1)
#
#
# def fat(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fat(x - 1)
#
#
# print(fat(3))


def fatorial(n: int) -> int:
    # Caso base
    if n == 1:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    fat5 = fatorial(5)
    print(fat5)

# from timeit import timeit
#
# for _ in range(5):
#     print('Recursão')
#
# print('---------------------')
#
#
# def recursao(i):
#     print('Recursão')
#     i += 1
#     if i == 5:
#         return
#     else:
#         recursao(i)
#
#
# recursao(0)
#
#
# def soma1(n):
#     soma = 0
#     for i in range(n+1):
#         soma += i
#     return soma
#

def soma2(n):
    if n == 0:
        return 0
    return n + soma2(n-1)


# soma1(100)
print(soma2(5))
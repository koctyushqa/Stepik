# Test
#
# def f(n):
#     return n * 10 + 5
#
# print(f(f(f(10))))
#
# a = f(f(f(10)))
# print(a)
#
# 10555


# TASK_29. Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
#
#         {    1−(x+2)^2 ,      при  x ≤ −2
# f(x) = {     −(x/2) ,         при −2 < x ≤ 2
#         {    (x−2)^2+1 ,      при  2 < x
# (Выше - одна большая скобка на 3 строки.)
#
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
#
# Sample Input 1:
# 4.5
# Sample Output 1:
# 7.25
# Sample Input 2:
# -4.5
# Sample Output 2:
# -5.25
# Sample Input 3:
# 1
# Sample Output 3:
# -0.5
#
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2

    elif -2 < x <= 2:
        return -(x/2)

    elif 2 < x:
        return (x - 2) ** 2 + 1


# print(f(4.5))

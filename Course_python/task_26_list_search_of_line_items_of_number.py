# Напишите программу, которая считывает список чисел lst из
# первой строки и число x из второй строки, которая выводит
# все позиции, на которых встречается число x в переданном списке lst.
#
# Позиции нумеруются с нуля, если число x не встречается в
# списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
#
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

# Пример:

# Ввод:
# 5 8 2 7 8 8 2 4
# 8
# Вывод:
# 1 4 5

# Ввод:
# 5 8 2 7 8 8 2 4
# 10
# Вывод:
# Отсутствует


lst = [int(i) for i in input("Введите числа: ").split()]
x = int(input("Введите число индексы которого вы ищете: "))
if x not in lst:
    print('Отсутствует')
for j in range(len(lst)):
    if lst[j] == x:
        print(j, end=' ')

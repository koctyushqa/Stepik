# Напишите программу, которая считывает со стандартного
# ввода целые числа, по одному числу в строке, и после
# первого введенного нуля выводит сумму полученных на вход чисел.

a = 0
while True:
    x = int(input("Введите число: "))
    a += x
    if x == 0:
        break
print(a)

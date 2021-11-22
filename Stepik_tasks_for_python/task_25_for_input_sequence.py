# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно).
# На вход программе передаётся положительное целое число
# n — столько элементов последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
#
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.


# Первый вариант:

a = int(input("Введите число: "))
b = 0
c = []
while len(c) < a:
    if c.count(b) < b:
        c.append(b)
    else:
        b += 1
    print(*c)


# Второй вариант:

a = int(input("Введите число: "))
c = 0
for i in range(a + 1):          # for i=1 in range(6):  # for i=2 in range(6):  # for i=2 in range(6):
    for j in range(i):          # for j=0 in range(1):  # for j=0 in range(2):  # for j=1 in range(2):
        c += 1                  # c = 1                 # c = 2                 # c = 3
        if c < a + 1:           # if 1 < 6              # if 2 < 6              # if 3 < 6
            print(i, end=' ')   # print 1               # print 2               # print 2

# for i=3 in range(6):  # for i=3 in range(6):  # for i=3 in range(6):  # for i=4 in range(6):  # for i=4 in range(6):
# for j=0 in range(3):  # for j=1 in range(3):  # for j=2 in range(3):  # for j=0 in range(4):  # for j=1 in range(4):
# c = 4                 # c = 5                 # c = 6                 # c = 7                 # c = 8
# if 4 < 6              # if 5 < 6              # if 6 < 6              # if 7 < 6              # if 8 < 6
# print 3               # print 3               # print 3               # print 4               # print 4

# print(c)   # 28
# print(j, end=' ')   # 0 0 1 0 1 2 0 1 2 3 0 1 2 3 4 0 1 2 3 4 5 0 1 2 3 4 5 6

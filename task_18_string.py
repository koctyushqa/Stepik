# GC-состав является важной характеристикой геномных последовательностей и определяется как процентное
# соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
# Напишите программу, которая вычисляет процентное содержание символов G
# (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание символов G и
# C равно 410⋅100=40.0, где 4 - это количество символов G и C,  а 10 - это длина строки.

# Первый вариант

stroka = input("Введите что-то: ")
odunak = stroka.upper()
koluch_GC = 0
dluna = 0

for i in odunak:
    dluna += 1
    if i == "G" or i == "C":
        koluch_GC += 1

print(koluch_GC/dluna * 100)


# Второй вариант

# a =  input() # input auto use type str
# s1 = a.upper().count('c'.upper())
# s2 = a.upper().count('g'.upper())
# S=s1+s2
# print(S/len(a)*100)

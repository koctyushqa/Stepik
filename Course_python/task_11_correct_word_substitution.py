# Недавно студенты из группы программистов написали для него программу,
# по которой робот, когда заходит в комнату, считает количество программистов
# в ней и произносит его вслух: "n программистов".
#
# Для того, чтобы это звучало правильно, для каждого n нужно использовать верное окончание слова.
#
# Напишите программу, считывающую с пользовательского ввода целое число n
# (неотрицательное), выводящее это число в консоль вместе с правильным образом
# изменённым словом "программист", для того, чтобы робот мог нормально общаться
# с людьми, например: 1 программист, 2 программиста, 5 программистов.
#
# В комнате может быть очень много программистов.
# Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.
#
# Дополнительный комментарий к условию:
# Обратите внимание, что задача не так проста, как кажется на первый взгляд.
# Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели
# какой-то из случаев входных данных (число программистов 0≤n≤1000). Обязательно
# проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания.
#
# Так как задание повышенной сложности, вручную код решений проверяться не будет.
# Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы
# используете только русские символы для ответа. В остальных случаях ищите ошибку в логике работы программы.

x = int(input("Сколько программистов в комнате? "))

if x == 0 or 5 <= x <= 20 or x in range(25, 1001, 10) or x in range(26, 1001, 10) or x in range(27, 1001,10) or x in range(28,1001,10) or x in range(29, 1001, 10) \
        or x in range(30, 1001, 10) or 111 <= x <= 114:
    print(x, "программистов")
elif x == 1 or x in range(21, 1001, 10):                    # elif чтобы не пересекалось с последним условием первого if
    print(x, "программист")
elif 2 <= x <= 4 or x in range(22, 1000, 10) or x in range(23, 1000, 10) or x in range(24, 1000, 10):
    print(x, "программиста")
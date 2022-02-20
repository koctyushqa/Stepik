# Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
#
# 1. конструктор __init__, принимающий произвольное количество аргументов.
# Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка;
# 2. переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
#    - "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой.
#         При этом значения должны быть упорядочены по возрастанию
#         (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
#    - "Пустой вектор", если наш вектор не хранит в себе значения.
#
# Пример :
# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2) # печатает "Пустой вектор"


class Vector:

    def __init__(self, *args):

        self.values = []
        for i in args:
            if isinstance(i, int):   # if type(i) == int:
                self.values.append(i)
        self.values.sort()

    def __str__(self):

        if len(self.values) != 0:
            return f"Вектор{*self.values,}"  # Тут важно убрать пробел после Вектор(по условию) и поставить запятую в конце
        else:
            return "Пустой вектор"


# v1 = Vector(1, 2, 3)
# print(v1)  # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2)  # печатает "Пустой вектор"
#
# Вектор(1, 2, 3)
# Пустой вектор

# Второй вариант :
# class Vector:
#     def __init__(self, *args):
#         self.values = args
#
#     @property
#     def values(self):
#         return self.__values
#
#     @values.setter
#     def values(self, value):
#         self.__values = [i for i in value if isinstance(i, int)]
#
#     def __str__(self):
#         if len(self.__values) == 1:
#             return f'Вектор({self.values[0]})'
#         elif self.__values:
#             return f'Вектор{tuple(sorted(self.__values))}'
#         return 'Пустой вектор'

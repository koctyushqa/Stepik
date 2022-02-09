# Создайте класс Person, у которого есть:
#
# 1. конструктор __init__, принимающий 3 аргумента: first_name, last_name, age.
# 2. метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
# 3. метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;
#
# Пример:
# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())  # выводит "Hendrix Jimi"
# print(p1.is_adult()) # выводит "True"


class Person:

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())              # выводит "Hendrix Jimi"
# print(p1.is_adult())               # выводит "True"
#
# Hendrix Jimi
# True

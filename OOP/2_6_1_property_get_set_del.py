class BankAccount:  # создание класса
    def __init__(self, name, balance):  # инициализация объекта и переменных
        self.name = name  # присвоение атрибуту класса self.name значение переменной name
        self.__balance = balance  # присвоение атрибуту класса self.__balance(делаем приватным) значение переменной balance

    def get_balance(self):  # метод получения баланса
        print('Баланс -', self.__balance)  # сообщение о балансе

    def set_balance(self, value):  # метод изменения баланса
        if not isinstance(value, (int, float)):  # проверяем, передано ли целое число или число с точкой
            raise ValueError('Баланс должен быть числом')  # если нет, то выводим сообщение (ошибку)
        self.__balance = value  # если число, то изменяем атрибут класса self.__balance на переданное значение в value
        print('Баланс изменён, остаток  - ', self.__balance)  # печатаем сообщение о изменении баланса

    def delete_balance(self):   # метод удаления баланса
        del self.__balance      # удаляем баланс
        print('Баланс удалён')  # уведомление после удаления баланса

    balance = property(  # используем функцию Property() для того чтобы сократить запись и повысить удобство работы с классом
        fget=get_balance,     # fget=get_balance устанавливаем метод просмотра(получения) баланса
        fset=set_balance,     # fset=set_balance устанавливаем метод изменения баланса
        fdel=delete_balance)  # fdel=delete_balance устанавливает метод удаления баланса


# acc1 = BankAccount('Pasha', 100)  # создаём экземпляр класса, и передаём имя и баланс
#
# acc1.balance
# acc1.balance = 5
# acc1.balance
# del acc1.balance
# acc1.balance = 18
# acc1.balance
#
# Баланс - 100
# Баланс изменён, остаток  -  5
# Баланс - 5
# Баланс удалён
# Баланс изменён, остаток  -  18
# Баланс - 18

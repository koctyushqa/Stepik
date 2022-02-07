# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
#
# В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент - значение,
# с которого начинается подсчет, по умолчанию равно 0
#
# Также нужно создать метод increment, который увеличивает счетчик на 1.
#
# Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>" и метод reset,
# который обнуляет экземпляр счетчика
#
# Пример работы с классом Counter
#
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"

class Counter:

    def start_from(self, value=0):
        self.value = value
        print(f"Счёт начинается с {value}")

    def increment(self):
        self.value += 1
        print(f"Добавили 1, теперь значение - {self.value}")

    def display(self):
        print(f"Текущее значение счетчика = {self.value}")

    def reset(self):
        self.value = 0
        print(f"Обнулили счётчик, значение равно {self.value}")


c1 = Counter()

c1.start_from(5)
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.reset()
c1.display()

# Счёт начинается с 5
# Добавили 1, теперь значение - 6
# Текущее значение счетчика = 6
# Добавили 1, теперь значение - 7
# Текущее значение счетчика = 7
# Обнулили счётчик, значение равно 0
# Текущее значение счетчика = 0

# Создайте класс Laptop, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно для
# экземпляра создать атрибуты brand, model,price и также атрибут laptop_name - строковое значение,вида "<brand> <model>"
#
# Прмиер:
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"
#
# И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.


class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} - {model}'   # brand + ' - ' + model   - тоже самое


laptop1 = Laptop('Asus', 'e-tyu5', 2100)
laptop2 = Laptop('Samsung', '13-bsdf0xx', 3500)

# hp = Laptop('hp', '15-bw0xx', 1800)
# print(hp.brand)
# print(hp.model)
# print(hp.price)
# print(hp.laptop_name)
#
# hp
# 15-bw0xx
# 1800
# hp - 15-bw0xx

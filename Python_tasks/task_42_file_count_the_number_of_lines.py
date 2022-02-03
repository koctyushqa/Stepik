import request

with open('03_06_02_input.txt') as in_f_obj:
    url = in_f_obj.read().strip()

r = request.get(url)
counter = 0

for line in r.text.splitlines():
    counter += 1

# Цикл выше можно заменить более простой конструкцией
# print(len(r.text.splitlines()))

with open('03_06_02_output.txt', 'w') as out_f_obj:
    out_f_obj.write(str(counter))

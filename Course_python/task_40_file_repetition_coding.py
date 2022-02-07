# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
#
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
#
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
#
# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка
# "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на
# компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у
# вас получится, надо отправить в качестве ответа на эту задачу.
#
# Sample Input:
#
# a3b4c2e10b1
# Sample Output:
#
# aaabbbbcceeeeeeeeeeb

# Первое :
digits = set('0123456789')
i = 0
multiplier = ''
decrypted = ''

with open('input.txt') as in_f_obj:
    string = in_f_obj.readline().strip()

char = string[i]
i += 1

while i < len(string):

    while string[i] in digits:
        multiplier += string[i]
        i += 1
        if i > (len(string) - 1):
            break

    # print(char * int(multiplier), end='')
    decrypted += (char * int(multiplier))

    multiplier = ''
    if i > (len(string) - 1):
        break
    char = string[i]

    i += 1

with open('output.txt', 'w') as out_f_obj:
    out_f_obj.write(decrypted)

# Второе :
# with open('input.txt', 'r') as f:
#     s = f.readline().strip()
# i = 0
# while i < len(s):
#     j = i + 1
#     while j < len(s) and s[j].isdigit():
#         j += 1
#     print(s[i] * int(s[i+1:j]), end='')
#     i = j

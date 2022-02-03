# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
#
# Попробуем написать подобную систему.
#
# На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются
# эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
#
# Sample Input:
#
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic
# Sample Output:
#
# stepic
# champignons
# the

# Первое :
text = set()
dictionary = {input().lower() for i in range(int(input()))}
for i in range(int(input())):
    for j in input().lower().split():
        text.add(j)
for i in text - dictionary:
    print(i)


# Второе :
# a = int(input())
# b = []
# for i in range(a):
#     x = input().lower()
#     if x not in b:
#         b.append(x)
#
# d = int(input())
# e = []
# for j in range(d):
#     x = input().lower().split()
#     for i in x:
#         if i not in b and i not in e:
#             e.append(i)
#
# print('\n'.join(e))

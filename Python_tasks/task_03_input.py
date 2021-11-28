# Катя узнала, что ей для сна надо X минут. В отличие от Коли,
# Катя ложится спать после полуночи в H часов и M минут. Помогите
# Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через
# X минут после того, как она ляжет спать.
#
# На стандартный ввод, каждое в своей строке, подаются значения X, H и M.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник:
# в первой строке часы, во второй — минуты.

x = int(input("Кате для сна, Х минут: "))
h = int(input("Катя ложится спать в H часов: "))
m = int(input("Катя ложится спать в M минут: "))

t = (0+h*60+m+x)
print(t // 60)
print(t % 60)

# Второй вариант
# X = int(input())
# H = int(input())
# M = int(input())
# print(((H*60)+X+M)//60)
# print((X+M)%60)
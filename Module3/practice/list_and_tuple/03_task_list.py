# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here
import random
n=int(input("Vvedite n:"))
numbers = []
summa=0
for i in range(n):
   numbers.append(random.randint(-10,10))
   summa = summa + i
print("summa=",summa)

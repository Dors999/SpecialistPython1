# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
n=int(input("Vvedite n:"))
numbers = []
summa=0
for i in range(n):
   numbers.append(random.randint(-100,100))
i=0
print(numbers)
while i<n:
    print(i)
    if numbers[i]%2==0 and numbers[i]>=0:
        summa=summa+numbers[i]
    i+=1
print("summa=",summa)

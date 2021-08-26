# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random

lst=[random.randint(0,20) for _ in range(20)]
print("spisok=",lst)
num=[el for el in lst if el>10]
print("kolichestvo=",len(num)+1)
sum=0
num=[el for el in lst if el>0]
for el in num:
    sum+=el
print("summa >0=",sum)
num=[el for el in lst if el%2==0]
print("spisok chetnyx=",num)
for el in num:
    sum+=el
print("Sr arih=",sum/(len(num)+1))

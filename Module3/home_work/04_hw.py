# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
import random
n=int(input("Vvedite n:"))
numbers = []
new_numbers=[]
for i in range(n):
   numbers.append(random.randint(-20,26))
i=0
temp=0
print(numbers)
while i<n:

    if numbers[i]>=0:
        if (numbers[i]**0.5)==int(numbers[i]**0.5):
            new_numbers.append(int(numbers[i]**0.5))

    i+=1
print("new nambers=",new_numbers)

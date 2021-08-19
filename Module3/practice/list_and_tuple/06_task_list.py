# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input("fist="))     # Первое число
second_number = int(input("second"))    # Второе число

# TODO: your code here
numbers=[]
while first_number<second_number:
    first_number+=1
    if first_number%3==0:
        print(first_number)
        numbers.append(first_number)
print(numbers)

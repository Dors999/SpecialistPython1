# Дано целое число. Определить, заканчивается ли оно число цифрой 5?
# Формат входных данных: Целое положительно число
# Формат выходных данных: Если число оканчивается цифрой 5, вывести «YES», в противном случае — вывести «NO».

number = int(input('Vvedite chislo: '))  # Считываем вещественное число
temp = number % 10
if temp==5:
    print("YES")
else:
    print("NO")

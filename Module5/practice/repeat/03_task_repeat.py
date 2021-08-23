# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    n1=number
    n2=0
    a=0
    while n1//1>0:
        n2=n2*10 +n1%10
        n1=n1//10
        a+=1
    return n2==number



a = 100
b = 130
num=0
for i in range(a,b):
    if palindrome(i):
        num+=1

print(num)

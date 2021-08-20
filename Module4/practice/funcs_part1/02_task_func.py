# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    pass
def palindrome(number):
    num=[]
    print(number)
    n1=number
    n2=0
    a=0
    while n1//1>0:
        n2=n2+(n1%10)*(10**a)
        n1=n1//10
        a+=1

    if n2==number:
        return "yes"
    else:
        return "no"






# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))

# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))

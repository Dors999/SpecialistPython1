# Напишите функцию находящую n-ое число Фибоначчи.
def fib(n):
    num_1=0
    num_2=1
    if n==1:
        return num_1
    elif n==2:
        return num_2
    elif n>2:
        for _ in range(2,n):
            num_buff = num_1 + num_2
            num_1 = num_2
            num_2 = num_buff
        return num_buff
print(fib(50))

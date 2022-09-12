#1 Выриант
n = int(input())
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)

#2 Вариант
n = int(input())
print(bin(n))
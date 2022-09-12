n = int(input("Введите число "))
fib1 = 0
fib2 = 1
i = 0
res = []
while i < n-1:
    fib_sum = fib1 - fib2
    fib1 = fib2
    fib2 = fib_sum
    res.append(fib2)   
    i = i + 1
res.reverse()    
fib3 = 0
fib4 = 1
i = 0
res1 = []
while i < n-1:
    fib_sum = fib3 + fib4
    fib3 = fib4
    fib4 = fib_sum
    res1.append(fib4)
    i = i + 1
print(*res,"0 1 0",*res1)    
    
   
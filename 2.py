lst = [2, 3, 4, 5, 6]
n = len(lst)
half = int(n/2) + 1
res = []
for i in range(half):
    first, last = lst[i], lst[n-i-1]
    res.append(first * last)
print(f'{lst}->{res}')    

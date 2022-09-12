lst = [1.1, 1.2, 3.1, 5, 10.01]
num_res = []
finish_res = 0
for i in range(len(lst)): 
    num_res.append(lst[i]%1)
    Max_v=max(num_res)
    Min_v=min(num_res)
print(f'{num_res}')

print(f'{Max_v-Min_v}')

        

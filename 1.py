list = [2, 3, 5, 9, 3]
Maxi=0
for i in range(len(list)):
    if list[i]%2==1:
        count = list[i]
        Maxi=Maxi+list[i]
        print(i+0,'число',count)
print(Maxi)        
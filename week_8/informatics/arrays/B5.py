n=int(input())

arr=[]

for i in range(n):
    arr[i].append(int(input()))

for i in range(n):
    if arr[i]%2==0:
        print(arr[i], sep=' ')
    
    
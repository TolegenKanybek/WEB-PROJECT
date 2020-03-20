n=int(input())
arr=[]
for i in range(n):
    arr[i].append(int(input()))

for i in range(n):
    if i<=n/2:
        arr[i]=arr[n-i-1]

for i in range(n):
    print(arr[i])
    

    
    
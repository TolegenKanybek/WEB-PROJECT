n=int(input())
arr=[]
cnt=0

for i in range(n):
    arr[i].append(int(input()))

for i in range(1,n):
    if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
        cnt=cnt+1
    
    
    
print(cnt)

    

    
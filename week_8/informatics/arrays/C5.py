n=int(input())

cnt=0
arr=[]

for i in range(n):
    arr[i].append(int(input()))

for i in range(n):
    if arr[i]>0:
        cnt=cnt+1


print(cnt)
        
    
    
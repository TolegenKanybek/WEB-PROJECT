n=int(input())

arr=[]
cnt=0

for i in range(n):
    arr[i].append(int(input()))

for i in range(n-1):
    if arr[i+1]<arr[i]:
        cnt=cnt+1
    
print(cnt)
    

        
    
    
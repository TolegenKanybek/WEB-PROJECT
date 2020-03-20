n=int(input())

arr=[]

for i in range(n):
    arr[i].append(int(input()))

ok=False

for i in range(n-1):
    if (arr[i+1]>0 and arr[i]>0) or (arr[i+1]<0 and arr[i]>0)    
        ok=True
        break



if ok==True:
    print("YES")
else:
    print("NO")


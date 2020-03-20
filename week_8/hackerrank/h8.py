n=int(input())


arr=[]
for i in range(n):
    arr[i].append(int(input()))


maxi=arr[0]

for i in range(n):
    if arr[i]>maxi:
        maxi=arr[i]

second_maxi=-1000

for i in range(n):
    if arr[i]>second_maxi and arr[i]<maxi:
        second_maxi=arr[i]


print(second_maxi)
    
    
    
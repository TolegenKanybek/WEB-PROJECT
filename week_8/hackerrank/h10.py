n = int(input())

results = {}


for i in range(n):
    a = input().split(' ')
    results[a[0]] = [float(x) for x in a[1:]]
student = input()

print (sum(results[student])/len(results[student]))
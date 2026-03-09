n = int(input())
a = list(map(int,input().split()))

a.sort()
sum = 0
result = 0
for i in range(n): 
    sum = sum + a[i]
    a[i] = sum

for j in range(n):
    result = result + a[j]

print(result)
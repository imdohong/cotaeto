n , m = map(int, input().split())

arr = []
j = 1
def backT(j):
    global n,m
    if(len(arr)==m):
        for i in range(m):
            print(arr[i], end=" ")
        print()
        return 
    for k in range(j,n+1):
        arr.append(k)
        backT(k)
        arr.pop()
        
backT(j)
a, b = map(int, input().split())

arr = []

def back():
    if len(arr) == b:
        print(*arr)
        return
    
    for i in range(1, a+1):
        arr.append(i)
        back()
        arr.pop()

back()
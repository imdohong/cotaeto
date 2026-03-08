t = int(input())
for _ in range(t):
    a= input().split()  
    
    result = float(a[0]) 
    
    for i in range(1, len(a)):
        if a[i] == '@':
            result *= 3
        elif a[i] == '%':
            result += 5
        elif a[i] == '#':
            result -= 7
    
    print(f"{result:.2f}")
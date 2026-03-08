t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    result = ""
    for char in s:
        result += char * r
    print(result)
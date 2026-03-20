
t=int(input(""))

for i in range(1, t+1):
    data=input().split()
    r=int(data[0])
    s=data[1]
    for k in range(0, len(s)):
        print(s[k]*r, end="")
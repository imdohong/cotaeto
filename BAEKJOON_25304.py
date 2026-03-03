total=int(input(""))
n=int(input(""))

for i in range(1, n+1):
    price, num=map(int, input().split())
    total-=price*num

if total==0:
    print("Yes")
else:
    print("No")

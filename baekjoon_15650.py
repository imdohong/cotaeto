n,m=map(int, input().split())
num=list()
start=1
def back_tracking(start):
    if len(num)==m:
        print(*num)
        return
    
    for i in range(start,n+1):
        num.append(i)
        back_tracking(i+1)
        num.pop()

back_tracking(start)
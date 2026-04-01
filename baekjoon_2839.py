n=int(input())
num=n
# 최대 n//3 번 n에서 3을 빼는 과정을 반복
count=0
if num%5==0:
    print(num//5)
elif num==3:
    print(1)
else:
    for i in range(int(n/3)):
        if num%5==0 and num>=5:
            print(count+(num//5))
            break
        # 루프를 반복했는데도 정확히 n킬로그램을 만들 수 없는 경우
        elif num<5 and (num-3)%5!=0:
            print(-1)
            break
        if i==int(n/3)-1 and num%3==0:
            print(count+1)
        num-=3
        count+=1
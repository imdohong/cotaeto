stu=[]
stu=[0]*30

for i in range(0, 28):
    num=int(input())

    stu[num-1]=num

for j in range(0, 30):
    if stu[j]==0:
        print(j+1)
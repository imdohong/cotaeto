import sys
input = sys.stdin.readline

mx_list = []
for i in range(9):
    i = list(map(int, input().split()))
    mx_list.append(i)
    

m_num = 0
position = (0,0)
for i in range(0, len(mx_list)):
    for j in mx_list[i]:
        if j > m_num :
            m_num = j
            position = (i+1, mx_list[i].index(j)+1)
            

print(m_num)
print(*position)

import sys
input = sys.stdin.readline

mx_list = []
for i in range(9):
    i = list(map(int, input().split()))
    mx_list.append(i)
    

m_num = 0
position = (1,1)
for i in range(0, 9):
    for j in range(9):
        current_val = mx_list[i][j]
        if current_val >= m_num :
            m_num = current_val
            position = (i+1, j+1)
            

print(m_num)
print(*position)

'''
# 다시 풀어 볼 문제

논리 오류
1. 최댓값이 0인 경우 고려 안함
2. 최댓값이 여러 개 존재하는 경우 index메서드 사용 시 첫 위치만 반환하므로 문제될 수 있음 
-> 직접적인 오류는 아니지만 출력 속도 느려짐

'''


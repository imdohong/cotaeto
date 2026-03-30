import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a_list = []
b_list = []
c_list = [[0]*m for _ in range(n)]

for i in range(n):
    a_input = list(map(int, input().split()))
    a_list.append(a_input)

for i in range(n):
    b_input = list(map(int, input().split()))
    b_list.append(b_input)
    
for i in range(n):
    for j in range(m):
        print(a_list[i][j] + b_list[i][j], end = ' ')
    print()
        
# 다시 풀어 볼 문제. 리스트 컴프리헨션 적극 활용할 것
# 2차원 배열 초기화 시 리스트 컴프리헨션 사용으로 편리하게 가능.
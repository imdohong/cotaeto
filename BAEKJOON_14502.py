import copy
from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    t = list(map(int,input().split()))
    arr.append(t)

ind_arr = []
ind2_arr = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ind_arr.append((i, j))
        elif arr[i][j] == 2:
            ind2_arr.append((i, j))

max_val = 0
arr2 = []
count = 0
test_arr = []
test_arr = copy.deepcopy(arr)
def count_zero(test_arr,n,m,max_val):
    count_zero = 0
    for i in range(n):
        for j in range(m):
            if(test_arr[i][j] == 0):
                count_zero = count_zero + 1
    if(max_val<count_zero): max_val = count_zero
    return max_val

def virus(test_arr, ind2_arr,n ,m):
    q = deque(ind2_arr)

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while q:
        x, y = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx and nx < n and 0<= ny < m):
                if(test_arr[nx][ny]==0):
                    test_arr[nx][ny] = 2
                    q.append((nx,ny))
    return test_arr

def wall(test_arr, arr2):
    for x, y in arr2:
        test_arr[x][y] = 1
    return test_arr
start = 0
def find_wall(start, ind_arr,arr,arr2,count):
    global max_val
    if(count == 3):
        test_arr = copy.deepcopy(arr)
        test_arr = wall(test_arr, arr2)
        test_arr = virus(test_arr,ind2_arr,n,m)
        max_val = count_zero(test_arr, n,m,max_val)
        return
    for i in range(start, len(ind_arr)):
        arr2.append(ind_arr[i])
        find_wall(i + 1, ind_arr,arr,arr2,count+1)
        arr2.pop()
find_wall(start, ind_arr,arr,arr2,0)
print(max_val)

# [연구소 문제 핵심 정리]

# 1. 문제 구조
# - 빈칸(0)에 벽 3개를 세운다
# - 바이러스(2)를 퍼뜨린다
# - 안전 영역(0)의 최대 개수를 구한다

# 2. 전체 알고리즘 흐름
# 1) 벽 3개 선택 → DFS (조합)
# 2) 바이러스 확산 → BFS
# 3) 안전 영역 개수 세기
# 4) 최대값 갱신

# 3. DFS (벽 세우기)
# - 벽은 순서가 의미 없음 → 조합 사용
# - start를 사용해서 중복 제거
# - i+1로 넘겨서 이미 선택한 인덱스는 다시 선택하지 않음
# 핵심: 이미 선택한 것보다 뒤에서만 고른다

# 4. BFS (바이러스 확산)
# - 퍼지는 문제 → BFS 사용
# - 큐에 초기 바이러스 위치 넣기
# - 감염되면 다시 큐에 넣어서 연쇄 확산
# 핵심: 퍼진 것도 다시 퍼진다

# 5. DFS에서 global을 쓰는 이유
# - DFS는 모든 경우를 탐색해야 함
# - return은 하나의 결과만 전달
# - 그래서 global 변수로 최대값 계속 갱신
# 핵심: DFS는 반환이 아니라 누적 갱신

# 6. 시간초과 해결 포인트
# - 순열 방식 → 같은 경우 중복 탐색
# - 조합 방식 → 중복 제거
# 예: A,B,C = B,A,C = C,B,A
# 해결: start 사용

# 7. 실수 포인트
# - 2차원 배열 접근: arr[i][j]
# - deepcopy 안 하면 원본 깨짐
# - BFS에서 범위 체크 필수
# - 함수 인자 순서 주의
# - global 안 쓰면 값 갱신 안됨

# 8. 한 줄 핵심
# - 벽은 DFS(조합), 확산은 BFS
# - 조합은 start, 확산은 queue
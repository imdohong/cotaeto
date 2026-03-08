import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))  

# 핵심 1
# 구간 문제는 대부분 "정렬"이 먼저 필요하다.
# 이유: 구간을 왼쪽 → 오른쪽 순서로 처리해야
# 이전 구간과 겹치는지 판단할 수 있기 때문
arr.sort()

# 핵심 2️
# 현재 유지하고 있는 구간
# 시작점과 끝점을 저장
start, end = arr[0]

length = 0

# 핵심 3️
# 이미 첫 구간을 start,end로 잡았기 때문에
# 두 번째 구간부터 확인
for x, y in arr[1:]:

    # 핵심 4️
    # 다음 구간의 시작점이 현재 끝점보다 왼쪽이면
    # 두 구간은 겹친다
    if x <= end:

        # 핵심 5️
        # 겹치면 더 멀리 있는 끝점으로 확장
        # (합집합을 만드는 과정)
        end = max(end, y)

    else:
        # 핵심 6️⃣
        # 안 겹치면 지금까지 구간 길이 확정
        length += end - start

        # 새로운 구간 시작
        start, end = x, y

# 핵심 7️
# 마지막 구간은 루프에서 더해지지 않으므로
# 마지막에 한 번 더 계산
length += end - start

print(length)
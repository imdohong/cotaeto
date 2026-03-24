n = int(input())
time = []
for i in range(n):
    t,p = map(int, input().split())
    time.append([t,p])
max = 0
calculate = []
count = 0

def time_calculate(calculate,count):
    global max
    sum = 0
    for j in range(len(calculate)):
        sum = sum + calculate[j][1] 
    if(max<sum): max = sum
        
    for i in range(count,n):
        t, q = time[i]
        if i + t <= n :
            calculate.append(time[i])
            next_idx = i + calculate[len(calculate)-1][0]
            time_calculate(calculate,next_idx)
            calculate.pop()
time_calculate(calculate,count)
print(max)
# 현재 상태도 하나의 완성된 선택 → 중간에서도 최대값이 나올 수 있음

# 끝까지 가야 최대가 되는 게 아님 → 중간에서 멈추는 경우가 최적일 수 있음

# n을 초과하는 순간에만 계산하면 일부 경우를 놓치게 됨

# 따라서 "들어오자마자 최대값 갱신"이 필요함

# 백트래킹은 선택할 때만 진행 → 조건(i + t <= n)을 만족할 때만 재귀

# 다음 인덱스는 i + t → 현재 상담 기간만큼 점프해야 함

# 모든 경우를 탐색하지만, 매 순간이 하나의 후보 상태임

# 리스트로 관리하면 매번 합 계산 필요 → 비효율 (개선: profit 변수로 누적)

# 이 문제는 "많이 선택"이 아니라 "잘 선택"이 핵심

# 종료 조건에 도달하지 않아도 최적해가 만들어질 수 있음
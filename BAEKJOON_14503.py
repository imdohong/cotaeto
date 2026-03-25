n , m = map(int, input().split())
r,c,d = map(int,input().split())
Mmap = []
for i in range(n):
    pos= list(map(int,input().split()))
    Mmap.append(pos)
result = 0
dx = [-1, 0, 1, 0]   
dy = [0, 1, 0, -1]
def clean_bot_move(Mmap):
    global dx, dy, result
    i, j, dir = r, c, d
    
    while(True):
        if(Mmap[i][j]==0):
            Mmap[i][j] = 2
            result += 1
            
        for k in range(4):
            dir = (dir+3)%4
            if_i, if_j = i + dx[dir], j + dy[dir]
            
            if 0 <= if_i < n and 0 <= if_j < m and Mmap[if_i][if_j] == 0:
                i, j = if_i, if_j
                break
        else:
            back_d = (dir + 2) % 4
            bi = i + dx[back_d]
            bj = j + dy[back_d]
            
            if not (0 <= bi < n and 0 <= bj < m) or Mmap[bi][bj] == 1:
                return
            i, j = bi, bj
    
clean_bot_move(Mmap)
print(result)
            
"""
[백준 14503 로봇 청소기 - 오답 및 핵심 개념 노트]

1. 상태값(방문 처리) 확실히 구분하기
   - 빈 칸(0)을 청소했다고 벽(1)과 똑같이 1로 덮어씌우면 안 됨!
   - 나중에 로봇이 후진할 때 청소한 공간을 벽으로 착각하게 되므로, 
     2나 -1 등 문제에서 주어지지 않은 아예 다른 숫자로 마스킹할 것.

2. 2차원 배열 좌표 계산 시 행(i/x)과 열(j/y) 오타 주의
   - 다음 좌표를 구할 때: if_i, if_j = i + dx[d], j + dy[d]
   - j(열) 자리에 i(행)를 더하는(i + dy[d]) 사소한 타이핑 실수 하나가 무한 루프를 만듦. 
   - 변수 이름 꼼꼼하게 확인하기!

3. 방향 전환 및 후진 시 모듈러(%) 연산 적극 활용하기
   - if-elif문으로 0, 1, 2, 3 방향을 일일이 하드코딩하면 코드가 길어지고 실수할 확률 증가.
   - 왼쪽 90도 회전: (현재 방향 + 3) % 4
   - 180도 후진 방향: (현재 방향 + 2) % 4
   - 미리 정의해둔 방향 배열(dx, dy)과 이 공식을 조합하면 10줄 넘는 코드를 단 두 줄로 압축 가능!

4. for-else 구문 활용 (Good Practice)
   - for문 안에서 break가 한 번도 걸리지 않고 끝까지 다 돌았을 때(즉, 4방향 모두 빈 공간이 없을 때) 
     자연스럽게 else문으로 넘어가서 후진 로직을 처리하는 방식은 아주 훌륭했음. 계속 써먹자!
"""
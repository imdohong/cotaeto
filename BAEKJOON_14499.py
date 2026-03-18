n, m, x, y, k = map(int, input().split())

arr = []
t = []
g = []
for i in range(n):
    t = list(map(int, input().split()))
    arr.append((t))
g = list(map(int, input().split()))

dice_high_num = 0
dice_pos = []
dice_width = []
dice_length = []
dice_width.append([0,0,0])
dice_length.append([0,0,0,0])
count = 0


def dice_rotation(n,x,y,dice_width,dice_length):
    w1 = dice_width[0][0] 
    w2 = dice_width[0][1]
    w3 = dice_width[0][2]
    l1 = dice_length[0][0]
    l2 = dice_length[0][1]
    l3 = dice_length[0][2]
    l4 = dice_length[0][3]
    if(n==1):
        dice_width[0][0] = w2
        dice_width[0][1] = w3
        dice_width[0][2] = l4
        dice_length[0][0] = l1
        dice_length[0][1] = w3
        dice_length[0][2] = l3
        dice_length[0][3] = w1
        y = y + 1
    elif(n==2):
        dice_width[0][0] = l4
        dice_width[0][1] = w1
        dice_width[0][2] = w2
        dice_length[0][0] = l1
        dice_length[0][1] = w1
        dice_length[0][2] = l3
        dice_length[0][3] = w3
        y = y - 1
    elif(n==3):
        dice_length[0][0] = l4
        dice_length[0][1] = l1
        dice_length[0][2] = l2
        dice_length[0][3] = l3
        dice_width[0][1] = l1
        x = x - 1
    else:
        dice_length[0][0] = l2
        dice_length[0][1] = l3
        dice_length[0][2] = l4
        dice_length[0][3] = l1
        dice_width[0][1] = l3

        x = x + 1
    return x,y

def dice_move(k,count,x,y,m,n,dice_width,dice_length,arr):
    while(k != count):
        move = g[count]
        if (move == 1 and y + 1 >= m) or (move == 2 and y - 1 < 0) or (move == 3 and x - 1 < 0) or (move == 4 and x + 1 >= n):
            count = count + 1
            continue
        x,y = dice_rotation(move,x,y,dice_width,dice_length)
        if(arr[x][y] != 0):
            dice_width[0][1] = arr[x][y]
            dice_length[0][1] = arr[x][y]
            arr[x][y] = 0
        else:
            dice_low_num = dice_length[0][1]
            arr[x][y] = dice_low_num
        dice_high_num = dice_length[0][3]
        print(dice_high_num)
        count = count + 1

dice_move(k,count,x,y,m,n,dice_width,dice_length,arr)
"""
💡 핵심 깨달음 1: "일단 움직이고 본다" vs "갈 수 있는지 보고 움직인다" (가장 큰 패착)
- 문제점: 예전 코드는 맵 밖으로 향하는 명령일 때, 주사위 배열을 이미 다 회전시켜버린 뒤에야 범위를 검사했다.
- 나비효과: 출력만 안 했을 뿐, 주사위는 이미 절벽 밑으로 떨어져 상태가 엉망이 되었고, 다음 턴부터 완전히 꼬여버림.
- 해결책: 주사위를 굴리기 전에 먼저 가상으로 다음 좌표(nx, ny)를 계산해보고, 안전한 땅(맵 안쪽)일 때만 진짜 좌표를 갱신하고 주사위 배열을 돌려야 한다!

💡 핵심 깨달음 2: 전개도를 가로/세로 배열로 나눴을 때의 '동기화' 문제
- 내가 짠 구조: 직관적인 전개도 모양대로 가로 3칸(dice_width), 세로 4칸(dice_length) 배열 사용.
  (인덱스 [0][1] = 바닥면, [0][3] = 윗면)
- 놓쳤던 점: 가로로 굴릴 때, 세로 배열에만 있던 '윗면(l4)' 데이터가 가로 배열로 내려와 합류해야 4면이 정상적으로 교대된다.
- 해결책: 한쪽 방향으로 굴린 직후에는, 반드시 두 배열이 공유하는 '바닥면'과 '윗면'의 값을 똑같이 맞춰주는(동기화) 작업이 필수!

💡 핵심 깨달음 3: 출력값의 위치 착각
- 지도의 값이 0일 때 (else문), 주사위 바닥면을 지도에 복사한 뒤 무의식적으로 '바닥면'을 출력하는 실수를 했다.
- 지도가 0이든 0이 아니든, 주사위가 한 번 정상적으로 굴러갔다면 무조건 상단(윗면, dice_length[0][3])을 출력해야 한다!
"""
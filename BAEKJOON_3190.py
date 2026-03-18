n = int(input())
k = int(input())
arr = []
for _ in range(k):
    x, y = map(int, input().split())
    arr.append([x, y])  
L = int(input())
arr2 =[]
for _ in range(L):
    x2, y2 = input().split()
    x2 = int(x2)
    arr2.append((x2, y2))  
snake_length = 1
snake_count = 0
snake_pos = []
snake_pos.append([1,1])
snake_tail_pos = []
snake_tail_pos.append([1,1])
snake_ang = 0
pos_i = 0
app_i = 0
def snake_angle(pos_i,arr2,snake_ang):
    if(arr2[pos_i][1]=="L"):
        if(snake_ang == 0):
            snake_ang = 90
        elif(snake_ang == 90):
            snake_ang = 180
        elif(snake_ang == 180):
            snake_ang = 270
        else:
            snake_ang = 0
    else:
        if(snake_ang == 0):
            snake_ang = 270
        elif(snake_ang == 90):
            snake_ang = 0
        elif(snake_ang == 180):
            snake_ang = 90
        else:
            snake_ang = 180
    pos_i = pos_i + 1
    return snake_ang, pos_i

def find_apple(arr,snake_pos):
    head = snake_pos[0]
    if(head in arr) :
        arr[arr.index(head)] = -1
        return 1
    else:
        return 0

def snake_move(n, pos_i, snake_tail_pos, snake_count, snake_pos,snake_ang):
    while(True):
        snake_count = snake_count + 1
        if(snake_ang == 0):
            snake_pos[0][1] = snake_pos[0][1] + 1
        elif(snake_ang == 90):
            snake_pos[0][0] = snake_pos[0][0] - 1
        elif(snake_ang == 180):
            snake_pos[0][1] = snake_pos[0][1] - 1
        else:
            snake_pos[0][0] = snake_pos[0][0] + 1
        if(snake_pos[0][0] > n or snake_pos[0][1] > n or snake_pos[0][0] < 1 or snake_pos[0][1] < 1 or ([snake_pos[0][0], snake_pos[0][1]] in snake_tail_pos[:-1])):
            break

        if(find_apple(arr,snake_pos) == 0):
                snake_tail_pos.append([snake_pos[0][0],snake_pos[0][1]])
                snake_tail_pos.pop(0)
        else:
            snake_tail_pos.append([snake_pos[0][0],snake_pos[0][1]])

        if(pos_i<L and arr2[pos_i][0] == snake_count):
            snake_ang, pos_i = snake_angle(pos_i,arr2,snake_ang)
    return snake_count
print(snake_move(n, pos_i, snake_tail_pos, snake_count, snake_pos,snake_ang))

"""
[ 파이썬 시뮬레이션 구현 시 주의사항 ]

1. 리스트와 튜플의 차이 (Mutability)
   - [x, y]는 수정 가능(Mutable)하지만, (x, y)는 수정 불가능(Immutable)함.
   - 좌표를 더하거나 뺄 때는 리스트 형태가 훨씬 다루기 편함.

2. 참조 복사(Shallow Copy)의 함정
   - snake_tail_pos.append(snake_pos[0]) 처럼 넣으면 주소값만 복사됨.
   - 머리가 움직이면 몸통 리스트 안의 모든 좌표가 같이 변하는 대참사가 발생.
   - 반드시 [snake_pos[0][0], snake_pos[0][1]] 처럼 '값'을 새로 만들어서 넣어야 함.

3. 리스트의 박스 구조 (Nested List)
   - snake_pos가 [[1, 1]] 형태라면, 실제 좌표는 snake_pos[0]에 있음.
   - if snake_pos in arr: (X) -> 박스 통째로 비교하면 절대 못 찾음.
   - if snake_pos[0] in arr: (O) -> 알맹이 좌표를 꺼내서 비교해야 함.

4. 시뮬레이션의 핵심: '로직의 순서' (Sequence)
   - 1초 증가 -> 머리 이동 -> [즉시 사망 확인] -> 꼬리 처리 -> 방향 전환 순서가 정석.
   - 사망 확인을 이동 직후에 하지 않으면, 1초가 밀리거나 죽어야 할 상황에 
     방향을 꺾어 살아남는 버그가 생김.

5. 함수 간의 값 전달 (Parameter & Return)
   - 숫자(int)는 함수 안에서 1을 더해도 바깥 변수에 영향을 주지 못함(복사본 전달).
   - 해결법: return snake_ang, pos_i 처럼 바뀐 값을 밖으로 던져서 덮어씌워야 함.

6. 리스트 활용 팁
   - 특정 값을 지울 때는 .remove(값)이 직관적.
   - 순서(맨 앞/맨 뒤)를 지울 때는 .pop(index)가 효율적.
   - 자기 몸 충돌 확인 시, 현재 머리를 제외한 슬라이싱(snake_tail_pos[:-1]) 활용.
"""
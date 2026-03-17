n = int(input())
k = int(input())
arr = []
for _ in range(k):
    x, y = map(int, input().split())
    arr.append((x, y))  
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
def snake_angle(pos_i,arr2,snake_angle):
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
    return snake_ang

def find_apple(arr,snake_pos):
    if((arr in snake_pos) == True):
        arr[arr.index(snake_pos)] = -1
        return 1
    else:
        return 0

def snake_move(n, snake_count, snake_pos):
    while(True):
        if(snake_pos == n or snake_pos==0 or (snake_pos in snake_tail_pos)):
            break
        
        if(snake_angle(pos_i,arr2,snake_angle) == 0):
            snake_pos[0][1] = snake_pos[0][1] + 1
            if(find_apple(arr,snake_pos) == 0):
                snake_tail_pos.append(snake_pos)
            snake_count = snake_count + 1
        elif(snake_angle(pos_i,arr2,snake_angle) == 90):
            snake_pos[0][0] = snake_pos[0][0] - 1
            if(find_apple(arr,snake_pos) == 0):
                snake_tail_pos.append(snake_pos)
            snake_count = snake_count + 1
        elif(snake_angle(pos_i,arr2,snake_angle) == 180):
            snake_pos[0][1] = snake_pos[0][1] - 1
            if(find_apple(arr,snake_pos) == 0):
                snake_tail_pos.append(snake_pos)
            snake_count = snake_count + 1
        else:
            snake_pos[0][0] = snake_pos[0][0] + 1
            if(find_apple(arr,snake_pos) == 0):
                snake_tail_pos.append(snake_pos)
            snake_count = snake_count + 1
    return snake_count
print(snake_move(n,snake_pos))
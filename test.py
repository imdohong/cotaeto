'''
import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
	return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(a, b)) # 7
print(lcm(a, b)) # 42
'''

'''
n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target
    if n<k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)
'''
'''
data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)
'''

'''
n = int(input())

fear = list(map(int, input().split()))
fear.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in fear:
    count +=1
    if count >= i:
        result += 1
        count = 0
        
print(result)

'''

'''

n = int(input())
x, y = 1, 1 # x, y 좌표가 아닌 행과 열
plan = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for s in plan:
    for i in range(len(move_types)):
        if s == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx > n or ny> n:
        continue
    x, y = nx, ny

print(x, y)
'''


'''
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1

print(count)    
'''
'''
current_point = input()
row = int(current_point[1])
col = int(ord(current_point[0])) - int(ord('a')) + 1

move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]
count = 0

for step in move:
    next_row = row + step[1]
    next_col = col + step[0]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count +=1

print(count)

'''
s = input()
result = 0
str_list = []

for i in s:
    if i.isalpha():
        str_list.append(i)
    else:
        result += int(i)
        
str_list.sort()
if result != 0:
    str_list.append(str(result))
    
print(''.join(str_list))
    
        
        
            
        
            
            



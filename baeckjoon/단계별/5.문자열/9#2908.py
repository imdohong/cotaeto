import sys
input = sys.stdin.readline

a, b = input().split()

a_list = list(a)
b_list = list(b)

a_list.reverse()
b_list.reverse()

num_a = ''
num_b = ''

for s in a_list:
    num_a += s

for s in b_list:
    num_b += s

if int(num_a) > int(num_b):
    print(num_a)
else:
    print(num_b)
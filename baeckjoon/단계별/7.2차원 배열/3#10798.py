import sys
input = sys.stdin.readline

word_list=[]
for row in range(5):
    row = list(input().rstrip())
    word_list.append(row)

for i in range(15):
    for j in range(5):
        if i < len(word_list[j]):
            print(word_list[j][i], end='')


    
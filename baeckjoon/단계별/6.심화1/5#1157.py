import sys
input = sys.stdin.readline

word = input().rstrip().upper()

used_char = list(set(word))
count_list =[]
for c in used_char:
    count_list.append(word.count(c))

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(used_char[count_list.index(max(count_list))])
    
# 다시 풀어 볼 문제
        
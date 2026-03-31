word=input()
word_upper=word.upper()

# 입력받은 문자열이 이루어진 알파벳을 알기 위한 집합 word_set
word_set=set(word_upper)

# (알파벳, 사용된 횟수) 순서쌍
count_list=list()
for i in word_set:
    # 알파벳 리스트
    count_list.append((word_upper.count(i), i))

print(count_list)

max=0
for i in range(1,len(count_list)):
    if count_list[i-1][0] <= count_list[i][0]:
        max=count_list[i][0]

for i in range(len(count_list)):
    if count_list.count(max)>2 :
        print("?")
    
print(max)
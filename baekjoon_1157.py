word=input()
word_upper=word.upper()

"""이루어진 알파벳을 알기 위해
중복되는 요소를 제거하는 set으로 감싼 뒤 
순서쌍을 이용하기 위해 리스트로 변경한다.
""" 
word_list=list(set(word_upper))

# (사용된 횟수, 알파벳) 순서쌍을 저장하기 위한 리스트
count_list=list()
for i in word_list:
    # (사용된 횟수, 알파벳) 순서쌍을 저장
    count_list.append((word_upper.count(i), i))

# 알파벳이 사용된 횟수 최대값 찾기
max_count=0
for count, alphabet in count_list:
    if max_count<count:
        max_count=count

# 찾은 최대값과 count가 같으면 max_alphas 리스트에 해당 alphabet을 저장
max_alphas=list()
for count, alphabet in count_list:
    if max_count==count:
        max_alphas.append(alphabet)

# max_alphas 리스트에 저장된 알파벳이 2개 이상이면 ? 출력
if len(max_alphas)>1:
    print("?")      
# 아니라면 알파벳 출력
else:
    print(max_alphas.pop())
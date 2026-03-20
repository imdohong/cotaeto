a=input("")
a.upper()

counts=[0]*26

for char in a:
    counts[ord(char)-ord('A')]+=1

max_count=max(counts)

if counts.count(max_count)>1:
    print("?")
else:
    max_index=counts.index(max_count)
    print(chr(max_index+ord('A'))) #숫자를 문자로 바꿔주는 내장함수 chr
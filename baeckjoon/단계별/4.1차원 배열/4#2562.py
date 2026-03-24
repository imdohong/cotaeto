nums = []
for i in range(0,9):
    n = int(input())
    nums.append(n)

for i in range(len(nums)):
    if nums[i] == max(nums):
        print(max(nums))
        print(i+1)
        
# 다시 풀어 볼 문제
# 마지막 for문 사용 안하고 list 메소드 index(value) 활용(처음 일치하는 리스트의 인덱스 출력)
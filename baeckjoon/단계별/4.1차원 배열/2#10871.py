n, x = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for i in nums:
    if i < x:
        print(i, end=" ")

# end 속성 사용으로 줄 바꿈 방지 가능 
# 다시 볼 문제
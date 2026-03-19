import sys

for i in sys.stdin:
    a, b = map(int, i.split())
    print(a + b)
# 1 == True. 파이썬에서 True 대신 1 사용 가능
# 다시 볼 문제. <힌트> 문제의 의도는 입력이 들어오지 않을 때 종료하도록 하기
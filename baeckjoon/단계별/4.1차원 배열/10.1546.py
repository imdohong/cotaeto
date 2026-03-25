n = int(input())
score = list(map(int, input().split()))
m = max(score)

for i in range(0,n):
    score[i] = score[i]/m * 100
    
    
avr = sum(score)/n
print(f"{avr:.6f}")
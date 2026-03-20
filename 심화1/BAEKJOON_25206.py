sum1, sum2 = 0, 0

for i in range(0, 20):
    line = input().split()
    if not line: break
    
    name, score, grade = line
    score = float(score)

    if grade == "P":
        continue

    sum2 += score

    if grade == "A+":
        sum1 += score * 4.5
    elif grade == "A0":
        sum1 += score * 4.0
    elif grade == "B+":
        sum1 += score * 3.5
    elif grade == "B0":
        sum1 += score * 3.0
    elif grade == "C+":
        sum1 += score * 2.5
    elif grade == "C0":
        sum1 += score * 2.0
    elif grade == "D+":
        sum1 += score * 1.5
    elif grade == "D0":
        sum1 += score * 1.0
    elif grade == "F":
        sum1 += score * 0.0

if sum2!= 0:
    print(sum1 / sum2)
else:
    print(0.0)
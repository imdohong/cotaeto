grade_table={"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0,
             "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

# 과목평점 딕셔너리를 통해 전공평점을 구한다.
grade_list=list()
sum_cred=0
for i in range(20):
    _,cred,grade=map(str, input().split())
    # 등급이 P일 경우 계산에서 제외한다.
    if grade!='P':
        grade_list.append(float(cred)*grade_table[grade])
        sum_cred+=float(cred)

print(sum(grade_list)/sum_cred)
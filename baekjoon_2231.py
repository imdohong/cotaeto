n_num=int(input())

# 반복의 하한선을 n_num//2로 잡음
"""각 자리가 9일 때 숫자의 합을 하한선으로 잡고 다시 수정할 것
n_num//2가 하한선인 것은 수학적인 근거 매우 부족
"""
for i in range(n_num//2, n_num):
    m=i
    m_num=0
    for j in str(i):
        m_num+=int(j)
    
    if n_num==m+m_num:
        print(m)
        break

    if i==n_num-1 and n_num!=m+m_num:
        print(0)
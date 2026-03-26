n, m=map(int, input().split())

matrix_a=[]
for i in range(n):
    row=list(map(int, input().split()))
    matrix_a.append(row)

matrix_b=[]
for i in range(n):
    row=list(map(int, input().split()))
    matrix_b.append(row)

for i in range(n):
    for j in range(m):
        print(matrix_a[i][j]+matrix_b[i][j], end=' ')
    print()




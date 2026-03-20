n=int(input())

for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1)+" "*(i-1))

for k in range(1, n):
    print(" "*k+"*"*(2*n-2*k-1)+" "*k)
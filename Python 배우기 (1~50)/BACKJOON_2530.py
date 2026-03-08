h,m,s = map(int, input().split())
d=int(input())
total = h*3600 + m*60 + s + d
h = (total//3600)%24
m = (total%3600)//60
s = total%60
print(h,m,s)
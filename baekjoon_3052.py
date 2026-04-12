alphas=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a=input()
a=a.replace('j','-').replace('=','-')
a=a.split('-')
print(a)
count=0
for i in alphas:
    if a in i:
        if a in 'dz=':
            continue
        count+=1

print(count)
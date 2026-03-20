alpha=input()
croatian=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in croatian:
    alpha=alpha.replace(char, '*')

print(len(alpha))
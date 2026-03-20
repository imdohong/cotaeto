n=int(input(""))
num=n

for i in range(1, n+1):
    word=input()
    for k in range(0, len(word)-1):
        if word[k]!=word[k+1]:
            if word[k] in word[k+1:]:
                num-=1
                break


print(num)
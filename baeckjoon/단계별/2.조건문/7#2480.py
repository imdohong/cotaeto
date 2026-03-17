a, b, c = map(int, input().split())
dice_list = [a, b, c]
dice_list.sort()

if len(set(dice_list)) == 1 :
    print(10000 + dice_list[0] * 1000)
elif len(set(dice_list)) == 2 :
    print(1000 + dice_list[1] * 100)
elif len(set(dice_list)) == 3 :
    print(dice_list[2] * 100)


# 다시 풀어볼 문제
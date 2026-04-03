def bs(low, high, num_list, target_num):
    # n_num에 m_num 리스트 내에 있는 수가 없으면 0 출력
    if low>high:
        return print(0)
    
    mid=(low+high)//2

    # 찾으려는 수가 n_num 리스트 중간값보다 큰 경우
    if num_list[mid]<target_num:
        return bs(mid+1, high, num_list, target_num)

    # 찾으려는 수가 n_num 리스트 중간값보다 작은 경우
    elif num_list[mid]>target_num:
        return bs(low, mid-1, num_list, target_num)
    
    # 찾았다!
    else:
        return print(1)

n=int(input())
n_num=[int(i) for i in input().split()]
m=int(input())
m_num=[int(i) for i in input().split()]

n_num.sort()

for i in m_num:
    bs(0, n-1, n_num, i)
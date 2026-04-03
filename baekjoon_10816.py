import sys
input = sys.stdin.readline

def start_index(card_list,target):
    low=0
    high=len(card_list)-1
    s_index=-1

    # 이분 탐색 반복 버전
    while low<=high:
        mid=(low+high)//2
        if card_list[mid]>target:
            high=mid-1
        elif card_list[mid]<target:
            low=mid+1
        # 왼쪽에 같은 값이 있는지 확인
        else:
            s_index=mid
            high=mid-1
    
    return s_index
        
def end_index(s_index, card_list, target):
    low=s_index
    high=len(card_list)-1
    e_index=0
    
    if s_index==-1:
        return -2
    
    while low<=high:
        mid=(low+high)//2
        if card_list[mid]>target:
            high=mid-1
        elif card_list[mid]<target:
            low=mid+1
        # 오른쪽에 같은 값이 있는지 확인
        else:
            e_index=mid
            low=mid+1

    return e_index

n=int(input())
n_card=[int(i) for i in input().split()]
m=int(input())
m_card=[int(i) for i in input().split()]

n_card.sort()

for i in m_card:
    s = start_index(n_card, i)
    e = end_index(s, n_card, i)
    print(e-s+1, end=" ")
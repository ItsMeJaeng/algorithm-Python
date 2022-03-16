#체육복

def solution(n, lost, reserve):
    borrowed = 0                                     # 몇 명이 빌렸는지 count

    lost_new = list(set(lost)-set(reserve))          # 여벌의 체육복을 가진 사람은 잃어버려도 있기 때문에 중복요소 제거
    reserve_new = list(set(reserve)-set(lost))

    for l in lost_new:                               # 앞 번호에 빌릴 사람이 있는지부터 탐색해야
        if l-1 in reserve_new:                       # 뒷 번호에 더 많은 친구가 빌릴 수 있는 가능성이 증가한다
            reserve_new.remove(l-1)
            borrowed += 1                            # 앞 번호 친구에게 빌렸으면 뒤에는 pass
        elif l+1 in reserve_new:
            borrowed += 1
            reserve_new.remove(l+1)

    return n - (len(lost_new)-borrowed)              # (총 학생 수) - {(잃어버린 총 학생 수) - (빌린 학생 수)}
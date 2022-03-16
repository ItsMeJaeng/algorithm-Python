#구명보트

def solution(people, limit):
    people.sort()
    boat = 0

    start = 0
    end = len(people)-1

    while start <= end:                          # 1. 가장 무거운 사람(마지막 사람)은
        boat += 1                                # 가장 가벼운 사람(가장 앞 사람)과 연결해야 태울 수 있는 확률이 증가한다.
        if people[start] + people[end] <= limit: # 2. 만약에 가장 무거운사람+가장 가벼운 사람을 태웠는데 여유가 있다면
            start += 1                           # 두번째로 가벼운 사람을 태워서 여유 무게를 최소화한 후 효율적으로 탈출시킨다.
        end -= 1                                 # 3. limit를 넘겼다면 무거운 사람만 태운다 (뒷 index만 앞으로 이동)
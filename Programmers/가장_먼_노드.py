#N으로 표현

def solution(N, number):
    all_case = [0,[N]]
    if N == number: #찾으려는 값과 N이 같으면 바로 반환
        return 1

    for nums in range(2, 9):
        temp = set() #중복되는 요소 제거
        temp.add(int(str(N)*nums)) #N이 연속되는 경우는 사칙연산이 아니므로 따로 추가 ex.55, 555, 5555

        for n_val in range(1,(nums//2)+1):
            for each_case in all_case[n_val]: #each_case와 twin_case를 더하면 n_val이 나와야 한다.
																							#ex) 4개의N의 조합은 [(1개의N의 조합) + (3개의N의 조합)] or [(2개의N의 조합) + (2개의N의 조합)] or [(3개의N의 조합) + (1개의N의 조합)]
																							# (1개의 N조합과 3개의 N조합) & (3개의 N조합과 1개의 N조합)은 동일하므로 위에서 (nums//2)+1만 탐색한 것
                for twin_case in all_case[nums-n_val]:
                    temp.add(each_case + twin_case)
                    temp.add(each_case * twin_case)
                    temp.add(each_case - twin_case)
                    temp.add(twin_case - each_case) #예외 사항을 위해 x-y, y-x 둘 다 처리
                    if twin_case != 0: #예외 사항을 위해 둘 다 처리
                        temp.add(each_case/twin_case)
                    if each_case != 0:
                        temp.add(twin_case/each_case)

        if number in temp: #nums개의 카드 수를 사용해서 조합하는 경우에서 찾으려는 값을 찾으면 반환
                return nums
        all_case.append(temp) #못 찾으면 모든 경우의 수에 append하고 다음 nums개의 카드 수에 대해 경우의 수 탐색

    return -1
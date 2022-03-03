#N으로 표현

def solution(N, number):
    all_case = [0,[N]]
    if N == number:
        return 1

    for nums in range(2, 9):
        temp = set()
        temp.add(int(str(N)*nums))

        for n_val in range(1,(nums//2)+1):
            for each_case in all_case[n_val]:
                for twin_case in all_case[nums-n_val]:
                    temp.add(each_case+twin_case)
                    temp.add(each_case*twin_case)
                    temp.add(each_case-twin_case)
                    temp.add(twin_case-each_case)
                    if twin_case != 0:
                        temp.add(each_case/twin_case)
                    if each_case != 0:
                        temp.add(twin_case/each_case)
        if number in temp:
                return nums
        all_case.append(temp)
    return -1
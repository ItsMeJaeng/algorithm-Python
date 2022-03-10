#정수 삼각형

def solution(t):
    for i in reversed(range(len(t)-1)): #reversed를 사용하면 큰 값에서 시작해서 0까지 iterate함
        for j in range(len(t[i])):
            t[i][j] += max(t[i+1][j], t[i+1][j+1])

    return t[0][0]
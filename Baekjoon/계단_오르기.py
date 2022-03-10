#계단 오르기

n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input())) #계단 층 별로 값 넣기

if n == 1 :
    print(stairs[1]) #계단이 1단만 있으면 바로 리턴
else:
    result = [0, stairs[1], stairs[1]+stairs[2]] #result는 각 단계별로 최댓값
    for i in range(3,n+1):
        result.append(max(result[i-2]+stairs[i], result[i-3]+stairs[i-1]+stairs[i]))
#3단 연속 밟을 수 없으므로 현재(i)번째 값을 더하려면 (2단계 전 최댓값)과 (이전 층 값+ 3단계 전 최댓값) 중 큰 값을 찾아야 한다.
    print(result[-1]) #마지막 요소(최댓값) 반환
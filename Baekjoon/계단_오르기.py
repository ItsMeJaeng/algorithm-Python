#계단 오르기

n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

if n == 1 :
    print(stairs[1])
else:
    result = [0, stairs[1], stairs[1]+stairs[2]]
    for i in range(3,n+1):
        result.append(max(result[i-2]+stairs[i], result[i-3]+stairs[i-1]+stairs[i]))
    print(result[-1])
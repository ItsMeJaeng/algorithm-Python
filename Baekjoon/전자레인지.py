#전자레인지

n = int(input())
dic = {300:0, 60:0, 10:0}

for i in dic:                       # 가장 큰 단위부터 채워야한다. 300초(5분)부터
    dic[i] = n//i                   # n초를 최대한 채우기 위해서 i초의 버튼을 몇 번 눌러야 하는지
    n -= (n//i)*i                   # 누른 초 만큼 n에서 빼준다 (남은 n초 계산)

if n == 0:                          # 딱 맞춰서 누를 수 있다면 dic안의 value값들을 출력
    for i in list(dic.values()):
        print(i, end=" ")
else:
    print(-1)                       # 그럴 수 없다면 -1 출력
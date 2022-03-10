#특정 거리의 도시 찾기

import heapq
import sys
import math

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)] 
dist = [math.inf] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)    #간선 연결(단방향). 거리가 모두 1이므로 거리정보는 저장하지 않는다

def solution(start):
    q = []
    heapq.heappush(q,[0, start]) #출발 노드와 현재 이동 거리인 0을 push한다
    dist[start] = 0              #출발 노드의 최소 거리는 0이므로 초기화 한다
    while q:
        distance, node = heapq.heappop(q)
        if distance > dist[node]:     #해당 if문을 적지 않아도 통과하지만 
		            continue          #if문을 통과하지 않는 경우에는 아래의 복잡한 for문을 거치지 않아서 시간적인 부분에서 더 효율적
        for g in graph[node]:
            cost = distance + 1
            if cost < dist[g]:        #현재 노드를 거쳐서 다음 g노드로 가는 것이 기존의 방식보다 더 효율적인 경우
                dist[g] = cost        #최솟값 업데이트
                heapq.heappush(q, [cost, g]) #다음 출발노드로 등록

solution(x)
check = True              #우선 true로 초기화
for i in range(1,n+1):
    if dist[i] == k:
        print(i)
        check = False     #한번이라도 k거리를 갖는 노드가 있는 경우 False로 바뀐다
if check:                 #만약 True면 k거리를 갖는 노드가 없으므로 0-1를 출력
    print(-1)
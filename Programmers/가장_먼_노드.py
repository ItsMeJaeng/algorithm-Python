#가장 먼 노드

import math
import heapq

def solution(n, edge):
    dist = [math.inf] * (n+1)
    dist[1] = 0   #첫 출발노드 초기화
    
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])  #grahp에 간선 연결 양방향이므로 a->b, b->a 모두 연결
    
    heap = []
    heapq.heappush(heap, [0, 1])  #출발노드 push
    while heap:                   #더 이상 탐색할 노드가 없으면 종료
        distance, node = heapq.heappop(heap) #탐색을 시작할 출발노드의 현재 최솟값과 노드 정보 입력
        for g in graph[node]:                #현재 node에서 갈 수 있는 다음 노드들 g에 대해 탐색
            if distance + 1 < dist[g]:       #만약 g의 기존 최솟값보다 현재 출발노드를 거쳐서가는 것이 더 효율적일 경우
                dist[g] = distance + 1       #g의 최솟값 업데이트
                heapq.heappush(heap, [distance + 1, g])  #g를 출발노드로하는 정보push

    return len([x for x in dist if x == max(dist[1:])])  #max(dist[1:])은 dist의 첫 0번 요소는 사용하지 않는 노드로 inf값을 가지므로 제외한다
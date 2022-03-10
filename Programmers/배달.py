#배달

import math
import heapq

def solution(N, road, K):
    dist = [math.inf] * (N+1)   #업데이트 할 거리정보를 무한대 값으로 초기화
    dist[1] = 0
    graph = [[] for _ in range(N+1)]

    for i in road:
        graph[i[0]].append([i[1],i[2]])
        graph[i[1]].append([i[0],i[2]])   #양방향 간선이므로 a,b의 경우 a->b, b->a 모두 연결


    heap = []
    heapq.heappush(heap, [0,1])   #(거리, 출발노드) => 첫 출발노드는 1이고 이동한 거리가 0

    while heap:                   #더 이상 탐색할 노드가 없을 때 까지
        distance, node = heapq.heappop(heap)
        for i in graph[node]:                                  #현재 출발노드에서 갈 수 있는 모든 노드에 대해서
            if distance + i[1] < dist[i[0]]:                   #탐색한 적 없거나  i 노드를 바로 방문하는 것보다 현재 노드를 거쳐서 가는 것이 더 효율적일 경우
                dist[i[0]] = distance + i[1]                   #dist정보를 개선된 값으로 업데이트
                heapq.heappush(heap, [distance + i[1], i[0]])  #다음 출발노드에 대한 정보와 현재의 최적값(최솟값) push

    return len([x for x in dist if x <= K])
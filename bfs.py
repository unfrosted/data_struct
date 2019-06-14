from collections import deque

VERTEX_COUNT = int(input('INPUT VERTEX COUNT: '))
EDGE_COUNT = int(input("INPUT EDGE COUNT: "))
BASE_DISTANCE = 1

graph = {vertex:set() for vertex in range(VERTEX_COUNT)}

distances = [None] * EDGE_COUNT
start_vertex = 0
distances[start_vertex] = 0

for element in range(EDGE_COUNT):
    vert_1, vert_2 = map(int, input('INPUT VERTEX: ').split())
    graph[vert_1].add(vert_2)
    graph[vert_2].add(vert_1)

queue = deque([start_vertex])
while queue:
    cur_vertex = queue.popleft()
    for neight_vertex in graph[cur_vertex]:
        if distances[neight_vertex] is None:
            distances[neight_vertex] = distances[cur_vertex] + BASE_DISTANCE
            queue.append(neight_vertex)
            
print(distances)

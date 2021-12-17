from collections import defaultdict
import heapq
from math import inf, sqrt

def reconstruct(predecessor, current):
    path = [current]
    while current in predecessor:
        current = predecessor[current]
        path = [current, *path]
    return path

def astar(start, goal, data):
    h = lambda p1, p2: p1[0]-p2[0] + p1[1]-p2[1]
    n, m = len(data), len(data[0])
    visited = set()
    predecessor = dict()
    gscore = defaultdict(lambda: inf, {start: 0})
    fscore = defaultdict(lambda: inf, {start: h(start, goal)})
    heap = []
    heapq.heappush(heap, (fscore[start], start))
    while heap:
        current = heapq.heappop(heap)[1]
        visited.add(current)
        if current == goal:
            return reconstruct(predecessor, goal)
        for dx, dy in zip((-1,0,1,0),(0,1,0,-1)):
            neighbor = (current[0]+dx, current[1]+dy)
            if neighbor in visited or neighbor[0] in (-1, n) or neighbor[1] in (-1, m):
                continue
            g_candidate = gscore[current] + data[neighbor[0]][neighbor[1]]
            if g_candidate < gscore[neighbor]:
                predecessor[neighbor] = current
                gscore[neighbor] = g_candidate
                fscore[neighbor] = g_candidate + h(neighbor, goal)
                heapq.heappush(heap, (fscore[neighbor], neighbor))

with open('input') as f:
    # part 1
    data = [[int(n) for n in l.rstrip()] for l in f.readlines()]
    dim = len(data)
    path = astar((0,0),(dim-1,dim-1),data)
    risk = sum(data[p[0]][p[1]] for p in path)-data[0][0]
    print("Part 1:", risk)

    # part 2
    ext = 5
    data_ext = [[(data[j][i]-1+nx+ny)%9+1 for nx in range(ext) for i in range(dim)] for ny in range(ext) for j in range(dim)]
    dim *= ext
    path = astar((0,0),(dim-1,dim-1),data_ext)
    risk = sum(data_ext[p[0]][p[1]] for p in path)-data_ext[0][0]
    print("Part 2:", risk)

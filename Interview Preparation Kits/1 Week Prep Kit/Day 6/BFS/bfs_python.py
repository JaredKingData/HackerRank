from collections import deque

def bfs(n, m, edges, s):
    graph = [[] for i in range(n)]
    for x, y in edges:
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
        
    visited = [False] * n
    distances = [-1] * n
    
    q = deque([(s-1, 0)])
    distances[s-1] = 0
    visited[s-1] = True
    
    while q:
        u, w = q.popleft()
        for v in graph[u]:
            if visited[v] == False:
                distances[v] = w + 6
                visited[v] = True
                q.append((v, w+6))
    
    # remove the distance of the starting vertex from the list
    distances.pop(s-1)
    
    return distances
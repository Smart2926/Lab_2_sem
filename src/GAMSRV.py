import heapq

def dejkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[neighbor] > cost + weight:
                dist[neighbor] = cost + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    
    return dist

def solve_gamsrv(n, m, clients, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  
    
    client_set = set(clients)
    min_max_delay = float('inf')
    
    for i in range(1, n + 1):
        if i in client_set:
            continue
        dist = dejkstra(n, graph, i)
        max_delay = max(dist[c] for c in clients)
        min_max_delay = min(min_max_delay, max_delay)
    
    return min_max_delay

def main():
    with open("gamsrv.in", "r") as f:
        lines = f.read().splitlines()
    
    n, m = map(int, lines[0].split())
    clients = list(map(int, lines[1].split()))
    edges = [tuple(map(int, line.split())) for line in lines[2:]]
    
    result = solve_gamsrv(n, m, clients, edges)
    
    with open("gamsrv.out", "w") as f:
        f.write(str(result) + "\n")
        
main()
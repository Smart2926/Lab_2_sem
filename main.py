import csv
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def read_adjacency_matrix(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        matrix = [list(map(int, row)) for row in reader]
    return matrix

def prim_mst(matrix):
    n = len(matrix)
    visited = [False] * n
    min_edge = [(0, 0, -1)]
    total_weight = 0
    mst_edges = []

    while min_edge:
        weight, u, prev = heapq.heappop(min_edge)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        if prev != -1:
            mst_edges.append((prev, u, weight))
        for v in range(n):
            if not visited[v] and matrix[u][v] > 0:
                heapq.heappush(min_edge, (matrix[u][v], v, u))

    return total_weight, mst_edges

def edge_list(matrix):
    edges = []
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                edges.append((i, j, matrix[i][j]))
    return edges

def draw_graph(edges, title="Граф", filename="graph.png", mst_edges=None):
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    weights = nx.get_edge_attributes(G, 'weight')

    edge_colors = []
    mst_set = set()
    if mst_edges:
        mst_set = {(min(u, v), max(u, v)) for u, v, _ in mst_edges}

    for u, v in G.edges():
        if (min(u, v), max(u, v)) in mst_set:
            edge_colors.append('red')
        else:
            edge_colors.append('gray')

    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos, with_labels=True, node_color='lightblue', node_size=700,
        font_weight='bold', edge_color=edge_colors, width=2
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

filename = "D:/Python/Sem_2/Lab_8/src/islands.csv"
matrix = read_adjacency_matrix(filename)

all_edges = edge_list(matrix)
total_weight, mst_edges = prim_mst(matrix)

draw_graph(all_edges, title="Повний граф з MST", filename="full_graph.png", mst_edges=mst_edges)

draw_graph(mst_edges, title="Мінімальне остовне дерево (MST)", filename="mst_graph.png")

print(f"Мінімальна довжина підводних кабелів: {total_weight}")

def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Посещаем текущую вершину
    visited.add(start)
    path.append(start)

    # Рекурсивный обход соседних вершин
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)

    return path

def create_graph(edges):
    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    return graph

# Входные рёбра
edges = [(4,2), (1, 3), (2, 4)]

# Создание графа из рёбер
graph = create_graph(edges)

# Стартовая вершина
start_vertex = 1

# Запуск алгоритма
path = dfs(graph, start_vertex)
print("Путь обхода: ", path)
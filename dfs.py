def dfs(graph, start, goal, visited=None, path=None):
    if start not in graph or goal not in graph:
        raise ValueError(f"Одна или обе вершины {start} и {goal} не существуют в графе.")

    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Посещаем текущую вершину
    visited.add(start)
    path.append(start)

    # Если достигнута целевая вершина
    if start == goal:
        return path

    # Рекурсивный обход соседних вершин
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result: # Если путь найден
                return result

    path.pop() # Если не найден путь через эту вершину, удаляем её из пути
    return None

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
start_vertex = 2
end_vertex = 4

# Запуск алгоритма
path = dfs(graph, start_vertex, end_vertex)

try:
    if path:
        print(f"Путь от вершины {start_vertex} до вершины {end_vertex}: {path}")
        print(f"Длина пути: {len(path) - 1}")
    else:
        print("Путь не найден")
except ValueError as e:
    print(f"Error: {e}")




# Comment for task, part 2
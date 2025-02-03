from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

'''
Для цього завдання я обрала візуалізацію транспортних зв’язків між районами міста Запоріжжя. 
Граф моделює, які райони мають безпосереднє сполучення між собою.
'''

graph = {
    'Вознесенівський': ['Дніпровський', 'Заводський', 'Комунарський', 'Олександрівський', 'Хортицький', 'Шевченківський'],
    'Дніпровський': ['Вознесенівський', 'Олександрівський', 'Хортицький', 'Шевченківський'],
    'Заводський': ['Вознесенівський'],
    'Комунарський': ['Вознесенівський', 'Олександрівський', 'Шевченківський'],
    'Олександрівський': ['Вознесенівський', 'Дніпровський', 'Комунарський', 'Хортицький', 'Шевченківський'],
    'Хортицький': ['Вознесенівський', 'Дніпровський', 'Олександрівський'],
    'Шевченківський': ['Вознесенівський', 'Дніпровський', 'Комунарський', 'Олександрівський']
}

G = nx.Graph(graph)

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10, font_weight='bold')
plt.title("Граф транспортної мережі районів міста")
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print(f"Кількість вершин (районів): {num_nodes}")
print(f"Кількість ребер (зв'язків між районами): {num_edges}")
print("Ступінь вершин (кількість сусідів кожного району):")
for node, degree in degree_dict.items():
    print(f"{node}: {degree}")


# Алгоритми
def dfs(graph, start_vertex):
    visited = set()
    stack = [start_vertex]  
    
    while stack:
        vertex = stack.pop()  
        
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
    
    return visited  


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue: 
        vertex = queue.popleft()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)

    return visited  


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph[current_vertex]:
            distance = distances[current_vertex] + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

dfs(graph, 'Вознесенівський')
bfs(graph, 'Вознесенівський')
print(dijkstra(graph, 'Вознесенівський'))

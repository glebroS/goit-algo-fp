import heapq


def dijkstra(graph, start):
    
    # Ініціалізація відстаней
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Пріоритетна черга (відстань, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

    # Створення графа
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    print(f"Найкоротші шляхи від вершини {start_node}:")
    for vertex, distance in shortest_paths.items():
        print(f"Відстань до {vertex}: {distance}")

    print("\nІнший приклад (більший граф):")
    graph2 = {
        'Київ': {'Житомир': 140, 'Полтава': 340, 'Чернігів': 150},
        'Житомир': {'Київ': 140, 'Рівне': 190, 'Вінниця': 130},
        'Полтава': {'Київ': 340, 'Харків': 140, 'Дніпро': 200},
        'Чернігів': {'Київ': 150, 'Суми': 180},
        'Рівне': {'Житомир': 190, 'Львів': 210},
        'Вінниця': {'Житомир': 130, 'Хмельницький': 120},
        'Харків': {'Полтава': 140, 'Дніпро': 220},
        'Дніпро': {'Полтава': 200, 'Харків': 220, 'Запоріжжя': 85},
        'Суми': {'Чернігів': 180, 'Харків': 190},
        'Львів': {'Рівне': 210},
        'Хмельницький': {'Вінниця': 120},
        'Запоріжжя': {'Дніпро': 85}
    }

    start_city = 'Київ'
    paths_from_kyiv = dijkstra(graph2, start_city)

    print(f"Найкоротші відстані від міста {start_city}:")
    for city, dist in paths_from_kyiv.items():
        print(f"{city}: {dist} км")

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

graph = {
    'start': {'A': 6, 'B': 2},
    'A': {'end': 1},
    'B': {'A': 3, 'end': 5},
    'end': {}
}
costs = {
    'A': 6,
    'B': 2,
    'end': float('inf')
}
parents = {
    'A': 'start',
    'B': 'start',
    'end': None
}
processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

def get_shortest_path(parents, start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = parents[current_node]
    path.append(start)
    path.reverse()
    return path

shortest_path = get_shortest_path(parents, 'start', 'end')

print("Shortest path costs:", costs)
print("Shortest path:", shortest_path)

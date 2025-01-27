from heapq import heappop, heappush

def a_star_search(graph, heuristics, start, goal):
    # Priority queue for open nodes
    open_set = []
    heappush(open_set, (0 + heuristics[start], 0, start, [start]))
    visited = set()

    while open_set:
        _, current_cost, current_node, path = heappop(open_set)

        print(f"Visiting: {current_node}")
        if current_node == goal:
            print(f"Goal reached: {goal}")
            print(f"Path: {path}")
            print(f"Cost: {current_cost}")
            return

        visited.add(current_node)

        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                total_cost = current_cost + cost
                estimated_cost = total_cost + heuristics[neighbor]
                heappush(open_set, (estimated_cost, total_cost, neighbor, path + [neighbor]))

# Input Parsing
n = int(input())
e = int(input())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(e):
    frm, to, cost = map(int, input().split())
    graph[frm].append((to, cost))

h = int(input())
heuristics = {}
for _ in range(h):
    node, heuristic = map(int, input().split())
    heuristics[node] = heuristic

start = int(input())
goal = int(input())

a_star_search(graph, heuristics, start, goal)

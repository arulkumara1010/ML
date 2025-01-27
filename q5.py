from queue import PriorityQueue

def parse_graph():
    # Parse nodes and costs
    node_costs = {}
    while True:
        line = input()
        if line.strip().lower() == "done":
            break
        node, cost = line.split()
        node_costs[node] = int(cost)
    
    # Parse edges
    graph = {}
    while True:
        line = input()
        if line.strip().lower() == "done":
            break
        parent, children = line.split(maxsplit=1)
        graph[parent] = {}
        for child in children.split(','):
            child_node, cost = child.split(':')
            graph[parent][child_node] = int(cost)
    
    return node_costs, graph

def ao_star(node_costs, graph, start, goal):
    # Priority queue for AO* search
    pq = PriorityQueue()
    pq.put((0, [start]))  # (cumulative cost, path)
    visited = set()
    
    while not pq.empty():
        cost, path = pq.get()
        current = path[-1]
        
        if current in visited:
            continue
        visited.add(current)
        
        # If goal is reached, return the path
        if current == goal:
            return " -> ".join(path)
        
        # Expand current node
        if current in graph:
            for neighbor, edge_cost in graph[current].items():
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    pq.put((new_cost, path + [neighbor]))
    
    return None

def main():
    # Parse input
    node_costs, graph = parse_graph()
    start = input().strip()
    goal = input().strip()
    
    # Perform AO* search
    result = ao_star(node_costs, graph, start, goal)
    if result:
        print(f"Shortest Path: {result}")
    else:
        print("No path found")

if __name__ == "__main__":
    main()

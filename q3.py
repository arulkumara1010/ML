from collections import defaultdict, deque

def bfs_lexicographical_order(n, edges, source):
    # Create the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Sort the adjacency list for lexicographical traversal
    for node in graph:
        graph[node].sort()
    
    # Perform BFS
    queue = deque([source])
    visited = set([source])
    bfs_order = []
    
    while queue:
        current = queue.popleft()
        bfs_order.append(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return " ".join(bfs_order)

def main():
    # Input
    n = int(input())  # Number of nodes
    m = int(input())  # Number of edges
    edges = [input().split() for _ in range(m)]
    source = input()  # Source node
    
    # Perform BFS traversal in lexicographical order
    result = bfs_lexicographical_order(n, edges, source)
    print(result)

if __name__ == "__main__":
    main()

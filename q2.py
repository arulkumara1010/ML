from collections import deque

def bfs_traversal(v, edges, source):
    # Create an adjacency list for the graph
    graph = [[] for _ in range(v)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)  # Since the graph is undirected
    
    # Perform BFS
    visited = [False] * v
    queue = deque([source])
    visited[source] = True
    bfs_order = []
    
    while queue:
        current = queue.popleft()
        bfs_order.append(current)
        
        # Visit all unvisited neighbors
        for neighbor in sorted(graph[current]):  # Sort to ensure consistent order
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return bfs_order

def main():
    # Input
    v, e = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    source = int(input())
    
    # Perform BFS and print result
    result = bfs_traversal(v, edges, source)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()

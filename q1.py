def find_paths(graph, source, destination, visited, current_path, all_paths):
    # If source is the destination, we have found a path
    if source == destination:
        all_paths.append(list(current_path))
        return

    # Mark the current node as visited
    visited[source] = True

    # Explore all the neighbors of the current node
    for neighbor in graph[source]:
        if not visited[neighbor]:
            current_path.append(neighbor)
            find_paths(graph, neighbor, destination, visited, current_path, all_paths)
            current_path.pop()  # Backtrack to explore other paths

    # Unmark the current node as visited for other paths
    visited[source] = False

def main():
    n = int(input())  # number of vertices
    m = int(input())  # number of edges

    # Initialize graph as adjacency list
    graph = [[] for _ in range(n)]

    # Input edges
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s = int(input())  # source vertex
    d = int(input())  # destination vertex

    visited = [False] * n  # to keep track of visited nodes
    current_path = [s]  # starting path with source node
    all_paths = []  # to store all found paths

    # Find all paths from source to destination
    find_paths(graph, s, d, visited, current_path, all_paths)

    # Output all the paths
    for path in all_paths:
        print(path)


if __name__ == "__main__":
    main()

from collections import deque
import heapq

# Function to parse the input file
def parse_input(file_name):
    with open(file_name, 'r') as file:
        grid_size = tuple(map(int, file.readline().strip().split(',')))
        start, goal = map(lambda x: tuple(map(int, x.split(','))), file.readline().strip().split(';'))
        obstacles = {tuple(map(int, coord.split(','))) for coord in file.readline().strip().split(';')}
        strategy = file.readline().strip().lower()
    return grid_size, start, goal, obstacles, strategy

# Utility to get neighbors
def get_neighbors(pos, grid_size, obstacles):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    neighbors = []
    for dx, dy in directions:
        new_pos = (pos[0] + dx, pos[1] + dy)
        if 1 <= new_pos[0] <= grid_size[0] and 1 <= new_pos[1] <= grid_size[1] and new_pos not in obstacles:
            neighbors.append(new_pos)
    return neighbors

# Depth First Search
def dfs(grid_size, start, goal, obstacles):
    stack = [start]
    visited = set()
    path = []
    cost = 0

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        path.append(current)
        visited.add(current)
        cost += 1
        if current == goal:
            break
        neighbors = get_neighbors(current, grid_size, obstacles)
        stack.extend(neighbors[::-1])  # Add neighbors in reverse for DFS
    return path, cost

# Breadth First Search
def bfs(grid_size, start, goal, obstacles):
    queue = deque([start])
    visited = set()
    path = []
    cost = 0

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        path.append(current)
        visited.add(current)
        cost += 1
        if current == goal:
            break
        neighbors = get_neighbors(current, grid_size, obstacles)
        queue.extend(neighbors)
    return path, cost

# A* Algorithm
def astar(grid_size, start, goal, obstacles):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    priority_queue = [(0 + heuristic(start, goal), 0, start)]
    visited = set()
    path = []
    cost = 0

    while priority_queue:
        _, g, current = heapq.heappop(priority_queue)
        if current in visited:
            continue
        path.append(current)
        visited.add(current)
        cost += 1
        if current == goal:
            break
        neighbors = get_neighbors(current, grid_size, obstacles)
        for neighbor in neighbors:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (g + 1 + heuristic(neighbor, goal), g + 1, neighbor))
    return path, cost

# Main function
def main(input_file):
    grid_size, start, goal, obstacles, strategy = parse_input(input_file)

    if strategy == "dfs":
        path, cost = dfs(grid_size, start, goal, obstacles)
    elif strategy == "bfs":
        path, cost = bfs(grid_size, start, goal, obstacles)
    elif strategy == "astar":
        path, cost = astar(grid_size, start, goal, obstacles)
    else:
        raise ValueError("Invalid strategy specified!")

    for block in path:
        print(block)
    print(f"Total search cost: {cost}")

# Run the program
if __name__ == "__main__":
    input_file = "input.txt"
    main(input_file)
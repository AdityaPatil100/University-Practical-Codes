from heapq import heappop, heappush

# Define the game grid and obstacles
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Define the possible movements (up, down, left, right, diagonal)
movements = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def heuristic(a, b):
    # Calculate the Manhattan distance as the heuristic function
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def astar(start, goal):
    open_set = []
    closed_set = set()
    g = {start: 0}
    f = {start: heuristic(start, goal)}
    parent = {}

    heappush(open_set, (f[start], start))

    while open_set:
        current = heappop(open_set)[1]

        if current == goal:
            # Reached the goal, construct the path
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        closed_set.add(current)

        for dx, dy in movements:
            neighbor = current[0] + dx, current[1] + dy
            tentative_g = g[current] + 1

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                if neighbor in closed_set and tentative_g >= g.get(neighbor, 0):
                    continue

                if tentative_g < g.get(neighbor, 0) or neighbor not in [i[1] for i in open_set]:
                    parent[neighbor] = current
                    g[neighbor] = tentative_g
                    f[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heappush(open_set, (f[neighbor], neighbor))

    # No path found
    return None

# Get user input for start and goal positions
start_pos = tuple(map(int, input("Enter start position (x, y): ").split()))
goal_pos = tuple(map(int, input("Enter goal position (x, y): ").split()))

# Run the A* algorithm
path = astar(start_pos, goal_pos)

if path:
    print("Path found:", path)
else:
    print("No path found.")

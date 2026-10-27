import heapq

def astar(maze, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    queue = [(heuristic(start, goal), 0, start, [start])]
    visited = set()
    while queue:
        _, cost, current, path = heapq.heappop(queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < len(maze) and
                0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] == 0 and
                neighbor not in visited):
                new_cost = cost + 1
                heapq.heappush(queue, (
                    new_cost + heuristic(neighbor, goal),
                    new_cost, neighbor, path + [neighbor]
                ))
    return None

maze = [[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]]
start, goal = (0, 0), (3, 3)
print("Shortest Path:", astar(maze, start, goal))

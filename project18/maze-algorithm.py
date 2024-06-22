def is_valid_move(maze, x, y, visited):
    """checking move is within bounds"""
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0 and not visited[x][y]

def dfs(maze, x, y, visited, path):
    
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        path.append((x, y))
        return True

    
    visited[x][y] = True

    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if is_valid_move(maze, new_x, new_y, visited):
            if dfs(maze, new_x, new_y, visited, path):
                path.append((x, y))
                return True

  
    visited[x][y] = False
    return False

"""maze"""
maze = [
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]


visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
path = []

"""Set start point"""
if dfs(maze, 0, 5, visited, path):
    path.reverse()
    print("Path found:", path)
else:
    print("No path found")

"""founded path"""
for i, j in path:
    maze[i][j] = 2

"""Result matrix"""
for row in maze:
    print(row)

from collections import deque

def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque()
    queue.append((start, [start]))

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        if visited[y][x]:
            continue
        visited[y][x] = True
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<cols and 0<=ny<rows and grid[ny][nx]!="W":
                queue.append(((nx, ny), path+[(nx, ny)]))
    return []

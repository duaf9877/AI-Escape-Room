def dfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    stack = [(start, [start])]

    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path
        if visited[y][x]:
            continue
        visited[y][x] = True
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<cols and 0<=ny<rows and grid[ny][nx]!="W":
                stack.append(((nx, ny), path+[(nx, ny)]))
    return []

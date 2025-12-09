import heapq

def a_star(grid, start, goal):
    def heuristic(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    open_set = []
    heapq.heappush(open_set, (heuristic(start,goal), 0, start, [start]))
    visited = set()
    while open_set:
        f,g,current,path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        x,y = current
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<len(grid[0]) and 0<=ny<len(grid) and grid[ny][nx]!="W":
                heapq.heappush(open_set, (g+1+heuristic((nx,ny),goal), g+1, (nx,ny), path+[(nx,ny)]))
    return []

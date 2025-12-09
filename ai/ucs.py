import heapq
def ucs(grid, start, goal):
    pq=[]
    heapq.heappush(pq,(0,start,[start]))
    visited=set()
    while pq:
        cost,current,path=heapq.heappop(pq)
        if current==goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        x,y=current
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(grid[0]) and 0<=ny<len(grid) and grid[ny][nx]!="W":
                heapq.heappush(pq,(cost+1,(nx,ny),path+[(nx,ny)]))
    return []

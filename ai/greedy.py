def greedy(grid, start, goal):
    path=[start]
    current=start
    while current!=goal:
        x,y=current
        options=[]
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(grid[0]) and 0<=ny<len(grid) and grid[ny][nx]!="W" and (nx,ny) not in path:
                dist=abs(nx-goal[0])+abs(ny-goal[1])
                options.append(((nx,ny),dist))
        if not options:
            break
        options.sort(key=lambda x:x[1])
        current=options[0][0]
        path.append(current)
    return path

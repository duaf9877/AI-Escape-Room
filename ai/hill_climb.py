import random
def hill_climb(grid):
    empty=[(x,y) for y,row in enumerate(grid) for x,t in enumerate(row) if t=="."]
    if len(empty)>=2:
        a,b=random.sample(empty,2)
        grid[a[1]][a[0]],grid[b[1]][b[0]]=grid[b[1]][b[0]],grid[a[1]][a[0]]
    return grid

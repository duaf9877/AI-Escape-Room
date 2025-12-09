import random
def genetic_algorithm(grid,generations=3):
    best=[row[:] for row in grid]
    for _ in range(generations):
        new=[row[:] for row in best]
        empty=[(x,y) for y,row in enumerate(new) for x,t in enumerate(row) if t=="."]
        if len(empty)>=2:
            a,b=random.sample(empty,2)
            new[a[1]][a[0]],new[b[1]][b[0]]=new[b[1]][b[0]],new[a[1]][a[0]]
            best=new
    return best

import random
from ai.bfs import bfs
from ai.dfs import dfs
from ai.a_star import a_star
from ai.ga import genetic_algorithm
from ai.hill_climb import hill_climb

class RoomGenerator:
    def __init__(self):
        self.start_pos = (0, 0)

    def generate_level(self, level):
        width, height = 7, 7
        # Start with empty grid
        grid = [["." for _ in range(width)] for _ in range(height)]

        # Place walls randomly
        for _ in range(level * 5):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            if (x, y) != (0, 0):
                grid[y][x] = "W"

        # Place Start and Exit
        grid[0][0] = "S"
        ex, ey = width - 1, height - 1
        grid[ey][ex] = "E"
        self.start_pos = (0, 0)

        # Place keys
        num_keys = level
        for _ in range(num_keys):
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                if grid[y][x] == ".":
                    grid[y][x] = "K"
                    break

        # Place traps
        for _ in range(level * 2):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            if grid[y][x] == ".":
                grid[y][x] = "T"

        # Ensure solvable using BFS
        path = bfs(grid, self.start_pos, (ex, ey))
        if not path:
            # if unsolvable, clear random walls
            for y in range(height):
                for x in range(width):
                    if grid[y][x] == "W":
                        grid[y][x] = "."

        # Apply GA + Hill Climb for variation
        grid = genetic_algorithm(grid, generations=3)
        grid = hill_climb(grid)

        # Return only two things: grid and player start position
        return grid, self.start_pos

    def count_keys(self, grid):
        """Count total keys in the grid."""
        return sum(row.count("K") for row in grid)

# Placeholder knowledge base data
PUZZLE_TYPES = ["key_door","trap","timed","maze","symbol"]
TRAP_TYPES = ["spike","pit","fire"]
REWARD_TYPES = ["key","bonus_points","time_bonus"]

# Example function to get random puzzle type
import random
def get_random_puzzle():
    return random.choice(PUZZLE_TYPES)

def get_random_trap():
    return random.choice(TRAP_TYPES)

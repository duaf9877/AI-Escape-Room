# engine/game_loop.py
import pygame
from engine.renderer import Renderer
from engine.input_handler import InputHandler
from rooms.generator import RoomGenerator

class GameLoop:
    def __init__(self):
        pygame.init()
        self.renderer = Renderer()
        self.input_handler = InputHandler()
        self.room_generator = RoomGenerator()
        self.level = 1
        self.grid, self.player_pos = self.room_generator.generate_level(self.level)
        self.keys_collected = 0
        self.total_keys = self.room_generator.count_keys(self.grid)
        self.hints = 3

    def move_player(self, dx, dy):
        x, y = self.player_pos
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(self.grid) and 0 <= nx < len(self.grid[0]):
            cell = self.grid[ny][nx]
            if cell != 'W':
                if cell == 'K':
                    self.keys_collected += 1
                    self.grid[ny][nx] = '.'
                elif cell == 'T':
                    # Trap: reset player to start
                    self.player_pos = self.room_generator.start_pos
                    return
                elif cell == 'D':
                    if self.keys_collected >= 1:
                        self.keys_collected -= 1
                        self.grid[ny][nx] = '.'
                    else:
                        return
                self.player_pos = [nx, ny]

    def check_exit(self):
        x, y = self.player_pos
        if self.grid[y][x] == 'E':
            self.level += 1
            if self.level > 6:
                print("Congratulations! You escaped all levels!")
                self.input_handler.quit = True
            else:
                self.grid, self.player_pos = self.room_generator.generate_level(self.level)
                self.keys_collected = 0
                self.total_keys = self.room_generator.count_keys(self.grid)

    def run(self):
        while not self.input_handler.quit:
            dx, dy = self.input_handler.handle_input()
            self.move_player(dx, dy)
            self.check_exit()
            self.renderer.draw_grid(self.grid, self.player_pos, self.level, self.keys_collected, self.total_keys, self.hints)
            self.renderer.update()
        pygame.quit()
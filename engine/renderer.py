import pygame
import os

class Renderer:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('AI Escape Room')
        self.clock = pygame.time.Clock()
        self.bg_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        # Load images once
        self.assets_path = "assets"
        self.player_img = pygame.image.load(os.path.join(self.assets_path, "player.png")).convert_alpha()
        self.key_img = pygame.image.load(os.path.join(self.assets_path, "key.png")).convert_alpha()
        self.exit_img = pygame.image.load(os.path.join(self.assets_path, "exit.png")).convert_alpha()
        self.trap_img = pygame.image.load(os.path.join(self.assets_path, "trap.png")).convert_alpha()
        self.wall_img = pygame.image.load(os.path.join(self.assets_path, "wall.png")).convert_alpha()
        self.floor_img = pygame.image.load(os.path.join(self.assets_path, "floor.png")).convert_alpha()

        # Map tile chars to images
        self.tile_images = {
            "S": self.floor_img,
            "E": self.exit_img,
            ".": self.floor_img,
            "W": self.wall_img,
            "K": self.key_img,
            "T": self.trap_img
        }

    def draw_grid(self, grid, player_pos, level, keys_collected, total_keys, hints):
        self.screen.fill(self.bg_color)
        rows = len(grid)
        cols = len(grid[0])
        tile_size = min(self.width // cols, self.height // rows)

        # Draw tiles
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                # Draw tile image
                img = self.tile_images.get(tile, self.floor_img)
                img_scaled = pygame.transform.scale(img, (tile_size, tile_size))
                self.screen.blit(img_scaled, rect.topleft)
                # Optional: draw grid lines
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

        # Draw player
        px, py = player_pos
        player_rect = pygame.Rect(px * tile_size, py * tile_size, tile_size, tile_size)
        player_img_scaled = pygame.transform.scale(self.player_img, (tile_size, tile_size))
        self.screen.blit(player_img_scaled, player_rect.topleft)

        # Draw info text
        info_text = f'Level: {level}   Keys: {keys_collected}/{total_keys}   Hints: {hints}'
        img = self.font.render(info_text, True, (255, 255, 255))
        self.screen.blit(img, (10, 10))

    def update(self):
        pygame.display.flip()
        self.clock.tick(30)

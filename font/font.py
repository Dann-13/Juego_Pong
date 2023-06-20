import pygame

class Font:
    def __init__(self, font_path, font_size):
        self.font_path = font_path
        self.font_size = font_size
        self.font = pygame.font.Font(self.font_path, self.font_size)

    def render_text(self, text, color, font_size=None):
        if font_size:
            font = pygame.font.Font(self.font_path, font_size)
        else:
            font = pygame.font.Font(self.font_path, self.font_size)
        return font.render(text, True, color)

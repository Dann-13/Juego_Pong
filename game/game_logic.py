import pygame
import pygame.image
from utils import constants

class GameLogic:
    def __init__(self):
         # Inicializar la lógica del juego
        self.font = pygame.font.Font('./font/FUTURISM.TTF', 50)
        self.is_scene_entered = False
        
    def draw_inicio(self, window, button_start, button_exit):
        text_surface = self.font.render("PONG WARS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH / 2, 200))
        window.blit(text_surface, text_rect)
        button_start.draw(window)
        button_exit.draw(window)
        
    def draw_juego(self, window, button_exit, images):
        image1 = images.load_image("./assets/Paleta1.png",50,220)
        images.draw_image(window, image1, 0, 100)
        image2 = images.load_image("./assets/Paleta2.png",50,220)
        x2 = constants.SCREEN_WIDTH - image2.get_width()
        images.draw_image(window, image2, x2, 100)
        button_exit.draw(window)
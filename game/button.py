import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.action = action

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        window.blit(text_surface, text_rect)
        
    def handle_event(self, event, game):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if self.text == "Iniciar juego":
                    print("¡Has hecho clic en el botón 'Comenzar juego'!")
                    self.action()
                    # Aquí puedes agregar la lógica para iniciar el juego
                elif self.text == "Salir":
                    print("¡Has hecho clic en el botón 'Salir'!")
                    # Aquí puedes agregar la lógica para salir del juego
                    self.action()
 
    

import pygame
from utils import constants
from game.button import Button

class Game:
    def __init__(self):
        # Inicializar Pygame
        pygame.init()
        # estado inicial del juego sera la pantalla de inicio
        self.current_scene='inicio'
        #Definimos las fuentes
        self.font = pygame.font.Font(None, 24)
        #Definimos el tamaño de la pantalla
        self.window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        #Definimos el titulo
        pygame.display.set_caption(constants.GAME_TITLE)
        #Los dos botones que tendremos
        self.button_start = Button(300, 325, 200, 50, "Iniciar juego",self.iniciar)
        self.button_exit = Button(300, 400, 200, 50, "Salir", self.exit)
        #Verificamos que al iniciar a un no hemos ingresado a la escena del juego
        self.is_scene_entered = False

    def run(self):
        # Bucle principal del juego
        running = True
        clock = pygame.time.Clock()

        while running:
            # Eventos del juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                self.button_start.handle_event(event, self)
                self.button_exit.handle_event(event, self)
            # Lógica del juego
            
            # Dibujar en la ventana
            self.window.fill((0, 0, 0))

            if self.current_scene == "inicio":
                self.button_start.draw(self.window)
                self.button_exit.draw(self.window)
            elif self.current_scene == "juego":
                # Mostrar contenido específico de la escena "juego"
                text_surface = self.font.render("¡Estás en la escena 'juego'!", True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2))
                self.window.blit(text_surface, text_rect)
                self.button_exit.draw(self.window)
            # Actualizar la ventana
            pygame.display.flip()

        pygame.quit()
        
    def exit(self):
        pygame.quit()
    
    def iniciar(self):
        self.current_scene = "juego"
        self.is_scene_entered = False
        print('iniciado juego')

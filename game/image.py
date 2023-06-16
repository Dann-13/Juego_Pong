import pygame
class Images:
    def __init__(self):
        self.images = {}

    def load_image(self, path, width=None, height=None):
        image = pygame.image.load(path)
        if width and height:
            image = pygame.transform.scale(image, (width, height))
        return image

    def draw_image(self, surface, image, x, y):
        surface.blit(image, (x, y))

    def draw_images(self, surface, image_list):
        for image_data in image_list:
            image = image_data['image']
            x = image_data['x']
            y = image_data['y']
            self.draw_image(surface, image, x, y)
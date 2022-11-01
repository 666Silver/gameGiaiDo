from tkinter import Image
from matplotlib import image
import pygame

hand = pygame.SYSTEM_CURSOR_HAND
class Button:
    def __init__(self, image, pos, callback):
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.callback = callback
 
    # Define function for normal button state
    def normal(self, image):
        self.image = image
        pygame.mouse.set_cursor()
 
    # Define function for mouse hover state
    def hover(self, image):
        self.image = image
        pygame.mouse.set_cursor(hand)
 
    # Define function for pressed state
    def pressed(self, image):
        self.image = image
    
    def draw_btn(self, surface):
        surface.blit(self.image, self.rect)
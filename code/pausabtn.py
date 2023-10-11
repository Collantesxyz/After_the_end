import pygame
import os
import sys
# Obtiene la ruta al directorio raíz del proyecto (GameAlexisLzL)
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_directorio)
from ahorrar import get_font

class PauseButton:
    def __init__(self, image, pos, text_input):
        # Inicializa los atributos de la clase PauseButton
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.text_input = text_input

        base_color = (255, 255, 255)
        hovering_color = (200, 200, 200)
        font_size = 36

        font = get_font(font_size)
        self.base_text = font.render(self.text_input, True, base_color)
        self.hover_text = font.render(self.text_input, True, hovering_color)

        if self.image is None:
            self.image = self.base_text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.hovered = False

    def update(self, screen):
        if self.hovered:
            self.image = self.hover_text
        else:
            self.image = self.base_text

        screen.blit(self.image, self.rect)

    def checkForClick(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False

    def changeColor(self, position):
        self.hovered = self.rect.collidepoint(position)

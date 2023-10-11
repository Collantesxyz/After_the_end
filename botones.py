from ahorrar import get_font
import pygame
import sys
from pygame.locals import MOUSEBUTTONDOWN
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        # Inicializa los atributos de la clase
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input

        # Renderiza el texto base y el texto de hover con el tamaño y color adecuados
        self.base_text = self.font.render(self.text_input, True, self.base_color)
        self.hover_text = self.font.render(self.text_input, True, self.hovering_color)

        # Si no se proporcionó una imagen, utiliza el texto base como imagen
        if self.image is None:
            self.image = self.base_text

        # Obtiene los rectángulos de la imagen y el texto
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        # Controla si el botón está siendo "hovered" (mouse sobre el botón)
        self.hovered = False

        # Velocidad de transición suave para el tamaño de fuente
        self.transition_speed = 2

    def update(self, screen):
        # Actualiza la imagen del botón según si está siendo "hovered" o no
        if self.hovered:
            self.image = self.hover_text
        else:
            self.image = self.base_text

        # Dibuja la imagen en la pantalla
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        # Verifica si la posición (generalmente la posición del mouse) está dentro del botón
        if self.rect.collidepoint(position):
            return True
        return False

    def changeColor(self, position):
        # Cambia el estado de "hovered" según si la posición está dentro del botón
        self.hovered = self.rect.collidepoint(position)

    def update_font_size(self, font_size):
        # Actualiza el tamaño de fuente de forma suave
        current_font_size = self.font.get_height()
        target_font_size = font_size

        if current_font_size < target_font_size:
            current_font_size += self.transition_speed
            if current_font_size > target_font_size:
                current_font_size = target_font_size
        elif current_font_size > target_font_size:
            current_font_size -= self.transition_speed
            if current_font_size < target_font_size:
                current_font_size = target_font_size

        # Actualiza la fuente y vuelve a renderizar el texto base y el texto de hover
        self.font = get_font(current_font_size)
        self.base_text = self.font.render(self.text_input, True, self.base_color)
        self.hover_text = self.font.render(self.text_input, True, self.hovering_color)

        # Actualiza el rectángulo del texto
        self.text_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

class PauseButton:
    def __init__(self, image, pos, text_input, font_size=36):
        # Inicializa los atributos de la clase PauseButton
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.text_input = text_input

        base_color = (255, 255, 255)
        hovering_color = (200, 200, 200)

        self.font = get_font(font_size)
        self.base_text = self.font.render(self.text_input, True, base_color)
        self.hover_text = self.font.render(self.text_input, True, hovering_color)

        if self.image is None:
            self.image = self.base_text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        # No cambiamos la imagen aquí, eliminamos el parpadeo
        screen.blit(self.image, self.rect)

    def checkForClick(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False

    def changeColor(self, position):
        # No necesitamos cambiar el color basado en hover
        pass

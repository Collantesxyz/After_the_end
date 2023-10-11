import pygame
import sys
import os
# Obtiene la ruta al directorio raíz del proyecto (GameAlexisLzL)
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_directorio)
from botones import Button
from ahorrar import get_font

  # Mueve la importación aquí

pygame.init()
PANTALLA = pygame.display.set_mode((1280, 720))



def ScreenNivel2():
    from ahorrar import idioma_actual
    MENU_TEXT = get_font(100).render("AFTER THE END NIVEL 2", True, "white")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
    pygame.display.set_caption(idioma_actual["options_titulo"])

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.fill("red")

        TEXTO_DE_START = get_font(45).render(idioma_actual["titulo_message"], True, "White")
        POSICIONTEXT = TEXTO_DE_START.get_rect(center=(640, 260))
        PANTALLA.blit(TEXTO_DE_START, POSICIONTEXT)

        PLAY_BACK = Button(
            image=None,
            pos=(640, 460),
            text_input=idioma_actual["back_button"],
            font=get_font(75),
            base_color="White",
            hovering_color="Green"
        )
        PANTALLA.blit(MENU_TEXT, MENU_RECT)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    # Regresar al menú principal en menu.py
                    from start import bienvenida
                    bienvenida()  # Llama a la función bienvenida() para iniciar la pantalla de bienvenida                                  
        pygame.display.update()

ScreenNivel2()  # Llama a la función main_menu() en menu.py
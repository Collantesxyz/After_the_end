# idiomasglobal.py
import sys
import pygame
import os
# Obtiene la ruta al directorio raíz del proyecto (GameAlexisLzL)
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_directorio)
from botones import Button
from ahorrar import get_font, IDIOMA
from ahorrar import idioma_actual,cambiar_idioma
pygame.init()
PANTALLA = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("AFTER THE END")


def mostrar_ventana_idioma():

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.blit(IDIOMA,(0,0))
        from ahorrar import idioma_actual
        MENU_TEXT = get_font(100).render("AFTER THE END", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        OPTIONS_TEXT = get_font(30).render(idioma_actual["lenguaje_message"], True, "White")
        POSICIONTEXT = OPTIONS_TEXT.get_rect(center=(160, 220))
        PANTALLA.blit(OPTIONS_TEXT, POSICIONTEXT)

        ESPANOL = Button(image=None, pos=(140, 290), 
                            text_input=idioma_actual["Idioma_ES"], font=get_font(30), base_color="#d7fcd4", hovering_color="Green")


        INGLES = Button(image=None, pos=(140, 340), 
                            text_input=idioma_actual["Idioma_IN"], font=get_font(30), base_color="#d7fcd4", hovering_color="Green")


        BRASIL = Button(image=None, pos=(140, 400), 
                            text_input=idioma_actual["Idioma_BR"], font=get_font(30), base_color="#d7fcd4", hovering_color="Green")


        RUSO = Button(image=None, pos=(140, 450), 
                            text_input=idioma_actual["Idioma_RU"], font=get_font(30), base_color="#d7fcd4", hovering_color="Green")


        OPTIONS_BACK = Button(image=None, pos=(50, 40), 
                            text_input=idioma_actual["back_button"], font=get_font(30), base_color="#d7fcd4", hovering_color="Green")

        PANTALLA.blit(MENU_TEXT, MENU_RECT)

        for button in [ESPANOL, RUSO, INGLES, BRASIL, OPTIONS_BACK]:
            font_size = (30)
            if button.rect.collidepoint(OPTIONS_MOUSE_POS):
                font_size = 45  # Tamaño más grande cuando el mouse está encima

            button.update_font_size(font_size)  # Actualizar el tamaño de fuente
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(PANTALLA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if ESPANOL.checkForInput(OPTIONS_MOUSE_POS):
                    cambiar_idioma("espanol")  # Cambia al idioma español
                if INGLES.checkForInput(OPTIONS_MOUSE_POS):
                    cambiar_idioma("ingles")  # Cambia al idioma inglés
                if BRASIL.checkForInput(OPTIONS_MOUSE_POS):
                    cambiar_idioma("brasil")  # Cambia al idioma portugués (brasil)
                if RUSO.checkForInput(OPTIONS_MOUSE_POS):
                    cambiar_idioma("ruso")  # Cambia al idioma portugués 
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    from opciones import options
                    options()
            pygame.display.update()


mostrar_ventana_idioma()
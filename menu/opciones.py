# idiomasglobal.py
import sys
import pygame
import os
# Obtiene la ruta al directorio raíz del proyecto (GameAlexisLzL)
ruta_directorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_directorio)
from botones import Button
from ahorrar import get_font
from ahorrar import idioma_actual,cambiar_idioma, OPCION


PANTALLA = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("AFTER THE END")

def options():
    global idioma_actual
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.blit(OPCION, (0, 0))
        from ahorrar import idioma_actual
        MENU_TEXT = get_font(100).render("AFTER THE END", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        OPTIONS_TEXT = get_font(30).render(idioma_actual["options_titulo"], True, "White")
        POSICIONTEXT = OPTIONS_TEXT.get_rect(center=(160, 220))
        PANTALLA.blit(OPTIONS_TEXT,  POSICIONTEXT)



        OPCION_IDIOMA = Button(image=None, pos=(120, 280), 
                            text_input=idioma_actual["languaje_button"], font=get_font(30), base_color="#d7fcd4", hovering_color="Green")


        OPCION_VOLUMEN = Button(image=None, pos=(120, 340), 
                            text_input="Volumen", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")


        OPTIONS_BACK = Button(image=None, pos=(50, 40), 
                            text_input=idioma_actual["back_button"], font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
        
        PANTALLA.blit(MENU_TEXT, MENU_RECT)

        for button in [ OPCION_IDIOMA, OPCION_VOLUMEN, OPTIONS_BACK]:
            font_size = 30
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
                if OPCION_IDIOMA.checkForInput(OPTIONS_MOUSE_POS):
                    from idiomasglobal import mostrar_ventana_idioma
                    mostrar_ventana_idioma()
                if OPCION_VOLUMEN.checkForInput(OPTIONS_MOUSE_POS):
                    from volumen import volumen1
                    volumen1()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    from prueba2 import main_menu
                    main_menu()

        pygame.display.update()



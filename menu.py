import pygame
import pygame_menu
import pygame_widgets
#инициализировали пакеты
pygame.init()
menuScreen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Menu') #задали название окна

#Функции кнопок меню
from alpha import start_the_game

#кастомизация темы
mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.title_background_color = (252, 130, 69)
mytheme.background_color = (255, 181, 112)
mytheme.widget_font_color = (255, 255, 255)

#создание меню
menu = pygame_menu.Menu('  Добро пожаловать     ', 400, 300,
                       theme=mytheme)

menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)

#запуск
# menu.mainloop(menuScreen)
while True:
    if menu.is_enabled():
        menu.mainloop(menuScreen)

    pygame.display.flip()
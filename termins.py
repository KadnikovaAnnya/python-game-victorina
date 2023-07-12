import pygame
import pygame_widgets
from pygame_widgets.button import Button

def termins():
    w = 800
    h = 570
    FPS = 30

    #settings
    BGCOLOR = (255, 255, 255)


    # создаем игру и окно
    pygame.init()
    sc = pygame.display.set_mode((w,h))
    clock = pygame.time.Clock()

    sc.fill(BGCOLOR)
    pygame.display.flip()
    pygame.display.update()
    pygame.display.set_caption('Victorina')

    test = True
    while test:
        # Ввод процесса (события)
        events = pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT :
                test=False
        # Обновление
        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()
        # Визуализация (сборка)

    #освобождение памяти и деинсталяция модулей pygame
    pygame.quit()
    quit()



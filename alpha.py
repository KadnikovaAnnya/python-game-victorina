import pygame
import pygame_menu
import pygame_widgets
from pygame_widgets.button import Button
def start_the_game():
# Pygame шаблон - скелет для нового проекта Pygame
    WIDTH = 800
    HEIGHT = 570
    FPS = 30

    #settings
    BGCOLOR = (255, 181, 112)
    HEADINGCOLOR = (119, 17, 0)

    # создаем игру и окно
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    screen.fill(BGCOLOR)
    pygame.display.update()
    pygame.display.set_caption('Victorina')

    #компоненты
    #Heading
    headingFont = pygame.font.Font('./fonts/PressStart.ttf', 48)
    heading = headingFont.render('Викторина!', True, HEADINGCOLOR,)
    screen.blit(heading, (175, 50))
    
    #функции кнопок
    from countries import countries
    from dates import dates
    from historyEvents import historyEvents
    from people import people
    from termins import termins

    #Buttons to choose category
    button1 = Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        100,  # X-coordinate of top left corner
        150,  # Y-coordinate of top left corner
        600,  # Width
        50,  # Height

        # Optional Parameters
        text='Термины',  # Text to display
        fontSize=48,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=termins  # Function to call when clicked on
    )

    button2 = Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        100,  # X-coordinate of top left corner
        220,  # Y-coordinate of top left corner
        600,  # Width
        50,  # Height

        # Optional Parameters
        text='Даты',  # Text to display
        fontSize=48,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=dates  # Function to call when clicked on
    )

    button3 = Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        100,  # X-coordinate of top left corner
        290,  # Y-coordinate of top left corner
        600,  # Width
        50,  # Height

        # Optional Parameters
        text='События',  # Text to display
        fontSize=48,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=historyEvents  # Function to call when clicked on
    )
    
    button4 = Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        100,  # X-coordinate of top left corner
        360,  # Y-coordinate of top left corner
        600,  # Width
        50,  # Height

        # Optional Parameters
        text='Великие люди',  # Text to display
        fontSize=48,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=people  # Function to call when clicked on
    )

    button5 = Button(
        # Mandatory Parameters
        screen,  # Surface to place button on
        100,  # X-coordinate of top left corner
        430,  # Y-coordinate of top left corner
        600,  # Width
        50,  # Height

        # Optional Parameters
        text='Страны',  # Text to display
        fontSize=48,  # Size of font
        margin=20,  # Minimum distance between text/image and edge of button
        inactiveColour=(200, 50, 0),  # Colour of button when not being interacted with
        hoverColour=(150, 0, 0),  # Colour of button when being hovered over
        pressedColour=(0, 200, 20),  # Colour of button when being clicked
        radius=20,  # Radius of border corners (leave empty for not curved)
        onClick=countries  # Function to call when clicked on
    )
    
    # Цикл игры
    running = True
    while running:
        # Ввод процесса (события)
        events = pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT :
                running=False
        # Обновление
        pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
        pygame.display.update()
        # Визуализация (сборка)

    #освобождение памяти и деинсталяция модулей pygame
    pygame.quit()
    quit()


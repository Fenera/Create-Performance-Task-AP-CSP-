import pygame
import sys
import random
import pygame_gui



pygame.init()
#pygame.font.init()

#Dimensions of the window
length = 1000
height = 600

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
sand = (255,205,116)
borange = (255,114,81)
modern3 = (14, 52, 91)
colors = [red, green, blue, white, black, sand, borange, modern3]

#Creates window
window = pygame.display.set_mode((length, height))
#Caption
pygame.display.set_caption("Testing")
#Initialize Font
font1 = pygame.font.SysFont("arialrounded", 50)

manager = pygame_gui.UIManager((length, height))

clock = pygame.time.Clock()
FPS = 60

text_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((150, 200), (700, 50)), manager = manager, object_id = "#main_text_entry")
run = True


#List to store questions





def display_text(text_display):
    while True:
    #background color
        window.fill(sand)
        new_text = pygame.font.SysFont("arial", 100).render(f"Answer: {text_display}", True, "black")
        new_text_rect = new_text.get_rect(center = (length/2, height/2))

        window.blit(new_text, new_text_rect)
        clock.tick(60)
        for event in pygame.event.get():
            #Program ends when 'x' pressed
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()



while run:

    refreshrate_ui = clock.tick(60)/750 #The /750 controls how fast the cursor blinks
    #background color
    window.fill(sand)
    #Refresh rate for UI
    #UI_RR = clock.tick(60)/1000


    for event in pygame.event.get():
        #Program ends when 'x' pressed
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
            display_text(event.text)

        manager.process_events(event)

    manager.update(refreshrate_ui)

    manager.draw_ui(window)




    test_text = font1.render("Which continent is the largest?", True, modern3)
    window.blit(test_text, (150, 50))
    clock.tick(60)
    pygame.display.update()
    

pygame.quit()



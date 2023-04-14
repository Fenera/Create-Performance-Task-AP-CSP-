import pygame
import sys
import random
import pygame_gui
from Question import quest_ans

#goals: get font to be corrected for each text placed on screen
#clean up code and create comments
#possibly a menu page
#scoreboard
#timer
#extraneous
#complete by 4/25

pygame.init()
#pygame.font.init()

#1. Create a seperate function that takes a question in 
#2. Use that function to display the question using GUI
#3. 





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

question_bank = ["Who was the first woman to fly solo across the Atlantic Ocean?", "What biological order do frogs belong to?", "What is your body's largest organ?", "What does GDP stand for?"]
answer_bank = ["amelia Earhart", "amphibians", "skin", "gross domestic product"]


def check_correct(question, response):
    if(quest_ans[question] == response.capitalize()):
        return True
    
def question_present():
    pass

def get_fitting_size(text):
    text_render = font1.render(text, True, modern3)
    rect_of_text = text_render.get_rect()
    text_width = rect_of_text.width
    while text_width > length - 100:
        text_width -= 15
    
    return text_width





def display_text(text_display, x, y, size):
    while True:
    #background color
        window.fill(sand)
        new_text = pygame.font.SysFont("arial", size).render(f"Your Answer: {text_display}", True, "black")
        new_text_rect = new_text.get_rect(center = (x ,y))

        window.blit(new_text, new_text_rect)
        clock.tick(60)
        for event in pygame.event.get():
            #Program ends when 'x' pressed
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()



question_index = 3
list_of_questions = list(quest_ans.keys())
question_answered = False
color_index = 0


while run:

    refreshrate_ui = clock.tick(60)/750 #The /750 controls how fast the cursor blinks
    #background color
    
    #Refresh rate for UI
    #UI_RR = clock.tick(60)/1000

    current_question = list_of_questions[question_index]
    size_of_question = get_fitting_size(current_question)

    question_on_screen = font1.render(current_question, True, modern3)
    window.blit(question_on_screen, (150, 50))
    clock.tick(60)
    

    for event in pygame.event.get():
        #Program ends when 'x' pressed
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
            if(check_correct(current_question, event.text)):
                display_text("Correct!! +1 point", 500, 300, 25)
                question_answered = True

            else:
                display_text(f"Incorrect!! The correct answer is '{quest_ans[current_question]}'", 500, 300, 25 )
                question_answered = True
                

            #event.text is what the user wrote and entered

        manager.process_events(event)

    if(question_answered):
        if(question_index < len(list_of_questions) - 1):
            question_index += 1
        else:
            question_index = 0
    if(color_index < len(colors) - 1):
        color_index += 1
    else:
        color_index = 0
    
    window.fill(colors[color_index])
    

    manager.update(refreshrate_ui)

    manager.draw_ui(window)



    
    

        
    pygame.display.update()
    

pygame.quit()

import pygame
import sys
import random
import pygame_gui
import time
from Question import quest_ans
import os

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


print(os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Dimensions of the window
length = 1000
height = 600

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
sand = (255,205,116)
boring_orange = (255,114,81)
ocean_blue = (14, 52, 91)
turquoise = (0,185,188)
coral = (255, 127, 80)
r_gray = (126,140,156)
premium_gray =  (171,195,205)
victory_green = (122,186,122)
blooming_red = (255,102,102)
colors = [red, green, blue, white, black, sand, boring_orange, ocean_blue]

#Creates window
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

#Caption
pygame.display.set_caption("Testing")



check_mark = pygame.image.load("check.png").convert_alpha()
check_mark = pygame.transform.scale(check_mark,(600, 600))
x_mark = pygame.image.load("incorrect.png").convert_alpha()
x_mark = pygame.transform.scale(x_mark, (600, 600))

#Initialize Font
font1 = pygame.font.SysFont("arialrounded", 50)
font3 = pygame.font.SysFont("arialrounded", 30)
font2 = pygame.font.SysFont("arialrounded,", 20)

manager = pygame_gui.UIManager((length, height))

clock = pygame.time.Clock()
FPS = 60


list_of_answers = ["(a)Come to a complete stop | (b)Yield to oncoming traffic | (c)Drive through the intersection",
                   "(a)Drive through with caution | (b)Drive through quickly | (c)Do not attempt to drive through it",
                   "(a)30mph | (b)25mph | (c)20mph",
                   "(a)Railroad crossing | (b)Construction zone | (c)Two way traffic",
                   "(a)Steer right | (b)Keep steering wheel straight | (c) Steer left",
                   "(a)Increase following distance | (b)Use highbeams | (c) Decrease following distance",
                   "(a)High beams | (b)Low beams | (c)Only fog lights",
                   "(a) Another vehicle is in your way | (b) It may help prevent a collision | (c) Animal on road",
                   "(a) Stop and proceed cautiously | (b) Slowly pass vehicles that seem to be stopped | (c) Look to the sides of your vehicle to see what is coming",
                   "(a)A depressant | (b)A stimulant | (c)Both",
                   "(a)Farther from the car ahead than normal | (b)No different than normal | (c)Closer to the car ahead than normal",
                   "(a)Sound your horn and maintain your speed | (b)Speed up to clear the area quickly | (c)Slow down and pass with caution",
                   "(a)Speed up | (b)Reduce your speed | (c)Drive at the posted speed",
                   "(a)Across from your vehicle | (b)Who arrived before you | (c)On your left",
                   "(a)During the first rain after a dry spell | (b)After it has been raining for awhile | (c)During a heavy downpour"]



text_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((500, 500), (, 50)), manager = manager, object_id = "#main_text_entry")


def correct_img(x, y):
    check_mark.set_alpha(255)
    #timer for 1 second(1000 millisecond)
    window.blit(check_mark, (x, y))
    #timer_sec = pygame.time.get_ticks() + 1000
    #while pygame.time.get_ticks() < timer_sec:
     #   window.blit(check_mark, (x, y))
    check_mark.set_alpha(0)
    return



def incorrect_img(x, y): 
    check_mark.set_alpha(255)   
    #timer for 1 second(1000 millisecond)
    window.blit(x_mark, (x, y))
    #timer_sec = pygame.time.get_ticks() + 1000
    #while pygame.time.get_ticks() < timer_sec:
    #    window.blit(x_mark, (x, y))
    x_mark.set_alpha(0)
    return

    



def check_correct(question, response):
    if(quest_ans[question].lower() == response.lower()):
        return True
    
def question_present():
    pass

def get_fitting_size(text):
    text_render = font1.render(text, True, ocean_blue)
    rect_of_text = text_render.get_rect()
    text_width = rect_of_text.width
    while text_width > length - 100:
        text_width -= 15
    
    return text_width


def display_text(text_display, x, y, size):
    while True:
        new_text = pygame.font.SysFont("arial", size).render(text_display, True, "black")
        new_text_rect = new_text.get_rect(center = (x ,y))

        window.blit(new_text, new_text_rect)
        clock.tick(60)
        for event in pygame.event.get():
            #Program ends when 'x' pressed
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()



question_index = 0
list_of_questions = list(quest_ans.keys())
question_answered = False
color_index = 0
number_correct = 0
number_incorrect = 0
lives = 3
run = True
test_if_end = False
list_ans_index = 0

while run:
    
    #background color
    window.fill(premium_gray)
    #Turquoise colored heading. Parameters = pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
    turq_rect = pygame.draw.rect(window, r_gray, (0,0, length, 65), 0)
    
    #Title
    text_title = font1.render("Mock Driving Test", True, black)
    window.blit(text_title, (length//2 - length//4.4, 6))
    




    refreshrate_ui = clock.tick(60)/750 #The /750 controls how fast the cursor blinks


    #Refresh rate for UI
    #UI_RR = clock.tick(60)/1000

    current_question = list_of_questions[question_index]
    size_of_question = get_fitting_size(current_question)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #correct_score = font2.render("Number Correct: " + str(number_correct), True, black)
    #incorrect_score = font2.render("Number Incorrect: " + str(number_incorrect), True, black)
    #window.blit(correct_score, (0,0))
    #window.blit(incorrect_score, (0, 35))
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    lives_display = font3.render("Chances: " + str(lives), True, black)
    window.blit(lives_display, (5, 5))

    question_on_screen = font3.render(current_question, True, black)
    answers_on_screen = font2.render(list_of_answers[list_ans_index], True, black)
    window.blit(answers_on_screen, (70, 200))
    window.blit(question_on_screen, (70, 120))
    clock.tick(60)
    

    for event in pygame.event.get():
        #Program ends when 'x' pressed
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    test_if_end = True
                    run = False
       
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
            if(check_correct(current_question, event.text)):
                #Makes the textbox empty 
                text_input.set_text("")
                #increments the list number_correct by 1 
                #!
                correct_img(100, 100)
                number_correct += 1
                #true if question has been answered
                question_answered = True
            else:
                incorrect_img(100, 100)
                text_input.set_text("")

                lives -= 1

                #increments the list number_incorrect by 1 
                #!
                number_incorrect += 1

                #true if question has been answered
                question_answered = True

            if(lives <= 0):
                test_if_end = True
                lives = 0
                window.fill(blooming_red)

                display_text("You Lost! You need more review.", 500, 300, 50)
                display_text("Click 'retry' for another go or 'Esc' to exit!", 500, 400, 35)
                
                
                   
            if(question_index < len(list_of_questions) - 1):
                question_index += 1
                list_ans_index += 1
            else:
                question_on_screen = font3.render("", True, black)
                window.blit(question_on_screen, (130, 120))
        

                #!
                #display_text("Final Score: " + str(number_correct) + "/" + str(len(list_of_questions)), 500, 300, 50)  
                # ! 
                test_if_end = True
                window.fill(victory_green)
                display_text("Congratulations! You have passed your practice test", 300, 300, 50)
                display_text("Click 'Esc' to exit", 500, 400, 35)
                time.sleep(3)

            #event.text is what the user wrote and entered

        manager.process_events(event)

    

    


    manager.update(refreshrate_ui)

    manager.draw_ui(window)



    
    
      

        
    pygame.display.update()
    

pygame.quit()

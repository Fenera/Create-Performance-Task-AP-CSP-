import pygame
import sys
import pygame_gui
import time
from Question import quest_ans
import os

#correct a c a b c a b b c a a c b b 
#incorrect b c b b c a b b c a

#Initialize the pygame module/library(1), Initializes the font class in pygame(2)
pygame.init()
pygame.font.init()

#This changes the directory of this python file to the file that it is being run out of(more portable from device to device)
#It allows me to easily load images in this file just by their name(ex: 'dog.png' instead of the actual direct-
# -ory of the image) 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Gets the dimensions/resolution of the screen the game is executed on
#ex. a screen with a resolution of 1920x1080 would be the stored in screen_information
screen_information = pygame.display.Info()

#length and height are set to the length and height of your screen(enables fullscreen usage)
length = screen_information.current_w
height = screen_information.current_h
print(length)
print(height)


#initialize all colors I can use in my program 
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

#Creates window/the box that the user interacts with
window = pygame.display.set_mode((length,height), pygame.FULLSCREEN)

#Caption of the window
pygame.display.set_caption("Testing")


#loads in two png images and scales them down for use in program
check_mark = pygame.image.load("check.png").convert_alpha()
check_mark = pygame.transform.scale(check_mark,(600, 600))
x_mark = pygame.image.load("incorrect.png").convert_alpha()
x_mark = pygame.transform.scale(x_mark, (600, 600))

#Initialize Fonts for later use using font class
font_largest = pygame.font.SysFont("arialrounded", 65)
font1 = pygame.font.SysFont("arialrounded", 50)
font3 = pygame.font.SysFont("arialrounded", 30)
font2 = pygame.font.SysFont("arialrounded,", 20)

#Creates a ui manager to be used in text box
manager = pygame_gui.UIManager((length, height))

#create a FPS system so the game executes smoothely(Frames refreshed per second)
clock = pygame.time.Clock()
FPS = 60


#This is a list of the answers that will be displayed on the screen
#They correlate to the questions in the Question.py file
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


#Create the textbox UI
#parameters -> pygame_gui.elements.UITextEntryLine(rectangle, (length, height)), manager = what ever your manager is set to, object_id = "#name of the entry field")
text_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 500), (1750, 100)), manager = manager, object_id = "#text_box_entry")


#If user got a correct answer, the a check mark will be shown with 0 transparency(255) and then become transparent(0)
def correct_img(x, y):
    check_mark.set_alpha(255)
    #timer for 1 second(1000 millisecond)
    window.blit(check_mark, (x, y))
    #timer_sec = pygame.time.get_ticks() + 1000
    #while pygame.time.get_ticks() < timer_sec:
     #   window.blit(check_mark, (x, y))
    check_mark.set_alpha(0)
    return


#If user got a incorrect answer, the an 'x' mark will be shown with 0 transparency(255) and then become transparent(0)
def incorrect_img(x, y): 
    check_mark.set_alpha(255)   
    #timer for 1 second(1000 millisecond)
    window.blit(x_mark, (x, y))
    #timer_sec = pygame.time.get_ticks() + 1000
    #while pygame.time.get_ticks() < timer_sec:
    #    window.blit(x_mark, (x, y))
    x_mark.set_alpha(0)
    return

    


#This taxes in a question and what the user responded with and checks if their answer matches with 
#the questions corresponding answer in the dictionary
def check_correct(question, response):
    if(quest_ans[question].lower() == response.lower()):
        return True
   

#Displays text that the user enters at the specified location and its font size
def display_text(text_display, x, y, size):
    while True:
        #Creates a font with the font size parameter
        #Text is rendered
        #Creates a rectangle limit/boundary for the text with the center being x and y
        new_text = pygame.font.SysFont("arial", size).render(text_display, True, "black")
        new_text_rect = new_text.get_rect(center = (x ,y))

        #displays that text
        window.blit(new_text, new_text_rect)
        
        #updates the window after text is loaded on screen
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
question_number = 1

while run:
    
    #background color
    window.fill(premium_gray)
    #Turquoise colored heading. Parameters = pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
    turq_rect = pygame.draw.rect(window, r_gray, (0,0, length, 75), 0)
    
    #Title of game created(1) then placed on screen(2)
    text_title = font_largest.render("Mock Driving Test", True, black)
    window.blit(text_title, (720, 28))

    text_exit = font_largest.render("Esc = Exit", True, black)
    window.blit(text_exit, (1700, 28))

    #tip to user
    text_tip = font3.render("*Enter the letter corresponding to the answer choice* Enter only the letters a, b, or c or else it will count as incorrect!", True, black)
    window.blit(text_tip,(100, 600))
    



    #The refresh rate of the text box
    refreshrate_ui = clock.tick(60)/750 #The /750 controls how fast the cursor blinks


    #Refresh rate for UI
    #UI_RR = clock.tick(60)/1000

    current_question = list_of_questions[question_index]
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #correct_score = font2.render("Number Correct: " + str(number_correct), True, black)
    #incorrect_score = font2.render("Number Incorrect: " + str(number_incorrect), True, black)
    #window.blit(correct_score, (0,0))
    #window.blit(incorrect_score, (0, 35))
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    lives_display = font1.render("Chances: " + str(lives), True, black)
    window.blit(lives_display, (5, 28))

    question_on_screen = font_largest.render(str(question_number) + ". " + current_question, True, black)
    answers_on_screen = font1.render(list_of_answers[list_ans_index], True, black)
    window.blit(answers_on_screen, (70, 300))
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
       
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#text_box_entry":
            if(check_correct(current_question, event.text)):
                correct_img(100, 100)
                #Makes the textbox empty 
                text_input.set_text("")
                #increments the list number_correct by 1 
                #!
                number_correct += 1
                #true if question has been answered
                question_answered = True
                question_number += 1
            if(not(check_correct(current_question, event.text))):
                incorrect_img(100, 100)
                text_input.set_text("")

                lives -= 1

                #increments the list number_incorrect by 1 
                #!
                number_incorrect += 1

                #true if question has been answered
                question_answered = True
                question_number += 1

            if(lives <= 0):
                test_if_end = True
                lives = 0
                window.fill(blooming_red)

                display_text("You Failed! You need more review.", 900, 300, 100)
                
                
                   
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
                display_text("Congratulations! You have passed your practice test", 900, 300, 100)


            #event.text is what the user wrote and entered

        manager.process_events(event)
        
    
        
        
    


    manager.update(refreshrate_ui)

    manager.draw_ui(window)



    
    
      

        
    pygame.display.update()
    

pygame.quit()

#*******************************************************************
#File 1: Main.py
#*******************************************************************


#Asset sources
#check mark downloaded from https://pngtree.com/freepng/green-check-mark-icon-design-template-vector_6219078.html 
#'x' mark downloaded from https://pngtree.com/freepng/red-x-fork_6001925.html
#import all the needed modules/libraries
import pygame
import sys
import pygame_gui
import time
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
font4 = pygame.font.SysFont("arialrounded", 40)

#Creates a ui manager to be used in text box
manager = pygame_gui.UIManager((length, height))

#create a FPS system so the game executes smoothely(Frames refreshed per second)
clock = pygame.time.Clock()
FPS = 60

#dictionary(list) that maps a question to its correct answer choice
quest_ans = {"What does a flashing red light indicate?": "a",
             "What should you do if you encounter a flooded roadway?": "c",
             "What is the speed limit in business and residential areas?": "b",
             "Signs with orange backgrounds mean:": "b",
             "If the rear end of your car starts skidding to the left, you should:" : "c",
             "When driving at night, you should: ": "a",
             "When driving in fog, rain, or snow, use:" : "b",
             "You should use your horn when: ": "b",
             "At intersections, crosswalks, and railroad crossings, you should always: " : "c",
             "Alcohol in any concentration is: " : "a",
             "If a road is slippery, maintain a following distance that is: " : "a",
             "You see pedestrians near the road. You should: " : "c",
             "If the roadway is wet or icy, you should: " : "b",
             "At an intersection with stop signs on all corners, yield the right-of-way to any driver: ": "b",
             "Roadways are the most slippery: " : "a"}

#This is a list of the answers that will be displayed on the screen
#They correlate to the questions in the Question.py file
list_of_answers = ["(a)Come to a complete stop | (b)Yield to oncoming traffic | (c)Drive through the intersection",
                   "(a)Drive through with caution | (b)Drive through quickly | (c)Do not attempt to drive through it",
                   "(a)30mph | (b)25mph | (c)20mph",
                   "(a)Railroad crossing | (b)Construction zone | (c)Two way traffic",
                   "(a)Steer right | (b)Keep steering wheel straight | (c) Steer left",
                   "(a)Increase following distance | (b)Use highbeams | (c) Decrease following distance",
                   "(a)High beams | (b)Low beams | (c)Only fog lights",
                   "(a)Another vehicle is in your way | (b) It may help prevent a collision | (c) Animal on road",
                   "(a)Stop and proceed cautiously | (b) Slowly pass vehicles that seem to be stopped | (c) Look to the sides of your vehicle to see what is coming",
                   "(a)A depressant | (b)A stimulant | (c)Both",
                   "(a)Farther from the car ahead than normal | (b)No different than normal | (c)Closer to the car ahead than normal",
                   "(a)Sound your horn | (b)Speed up to clear the area quickly | (c)Slow down and pass with caution",
                   "(a)Speed up | (b)Reduce your speed | (c)Drive at the posted speed",
                   "(a)Across from your vehicle | (b)Who arrived before you | (c)On your left",
                   "(a)During the first rain after a dry spell | (b)After it has been raining for awhile | (c)Heavy downpour"]


#Create the textbox UI
#parameters -> pygame_gui.elements.UITextEntryLine(rectangle, (length, height)), manager = what ever your manager is set to, object_id = "#name of the entry field")
text_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 500), (1750, 100)), manager = manager, object_id = "#text_box_entry")


#If user got a correct answer, the a check mark will be shown with 0 transparency(255) and then become transparent(0)
def correct_img(x, y):
    
    check_mark.set_alpha(255)
    #placed on screen
    window.blit(check_mark, (x, y))
    #transparency on
    check_mark.set_alpha(0)
    
    return


#If user got a incorrect answer, the an 'x' mark will be shown with 0 transparency(255) and then become transparent(0)
def incorrect_img(x, y): 
    #no transparency
    check_mark.set_alpha(255)
    #placed on screen
    window.blit(x_mark, (x, y))
    #transparency on
    x_mark.set_alpha(0)

    return

    


#This takes in a question and what the user responded with and checks if their answer matches with 
#the questions' corresponding answer in the dictionary
def check_correct(question, response):
    if(quest_ans[question].lower() == response.lower()):
        return True
   

#Displays text that the user enters at the specified location and with its font size
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


#Variable to store index of the question
question_index = 0
#The question side of the dictionary imported is converted to a list
list_of_questions = list(quest_ans.keys())
#lives/chances initialized
lives = 3
#variable that stores boolean value that will be used to control if the main loop will run or end
run = True
#variable to store the index of the answers shown on the screen
list_ans_index = 0
#stores the question number(ex. "1. What is the date")
question_number = 1

#main loop 
while run:
    
    #background color is set 
    window.fill(premium_gray)
    #Turquoise colored heading. Parameters = pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
    turq_rect = pygame.draw.rect(window, r_gray, (0,0, length, 75), 0)
    
    #Title of game created(1) then placed on screen(2)
    text_title = font1.render("Mock Driving Test", True, black)
    window.blit(text_title, (700, 15))

    #Text created to inform the user how to exit the program(1), text placed on screen(2)
    text_exit = font1.render("Esc = Exit", True, black)
    window.blit(text_exit, (1600, 15))

    #Text created to give a tip to the user(1), that text is placed on the screen(2)
    text_tip = font2.render("*Enter the letter corresponding to the answer choice* Enter only the letters a, b, or c or else it will count as incorrect!", True, black)
    window.blit(text_tip,(100, 600))
    



    #The refresh rate of the text box(the cursor blink)
    refreshrate_ui = clock.tick(60)/750 #The /750 controls how fast the cursor blinks(it slows it down)


    #The current question is stored in the variable and is decided by the question_index initialized outside the loop
    current_question = list_of_questions[question_index]

    #Text to show chances is created(1), that text is displayed on the screen(2)
    lives_display = font1.render("Chances: " + str(lives), True, black)
    window.blit(lives_display, (5, 15))

    #The text for the question shown on the screen is created
    question_on_screen = font_largest.render(str(question_number) + ". " + current_question, True, black)
    #The text for the answer choices on the screen is created
    answers_on_screen = font4.render(list_of_answers[list_ans_index], True, black)
    #The answer is placed on the screen
    window.blit(answers_on_screen, (70, 300))
    #The question is placed on the screen
    window.blit(question_on_screen, (70, 120))
    #The FPS variable is used to control the refresh rate of the loop
    clock.tick(FPS)
    
    #gets ever event that occurs(an event can be anything--button clicked--mouse clicked..etc)
    for event in pygame.event.get():
        #Program ends when 'x' pressed or exit is clicked
        if event.type == pygame.QUIT:
            run = False
        #if the user presses the escape key, the program will terminate
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        #checks if the user has clicked the text box AND entered a value
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#text_box_entry":
            #checks if their response is the correct answer to the question
            if(check_correct(current_question, event.text)):
                #A checkmark is shown on the screen
                correct_img(100, 100)
                #Makes the textbox empty(so previous answer is not shown for next question) 
                text_input.set_text("")
                #The question number is incremented by 1(question 1, 2, 3, 4..)
                question_number += 1

            #if their answer is incorrect
            else:
                #'x' mark is shown on the screen
                incorrect_img(100, 100)
                #Makes the textbox empty(so previous answer is not shown for next question)
                text_input.set_text("")
                #The lives(represents chances) is decremented by 1
                lives -= 1
                #The question number is incremented by 1(question 1, 2, 3, 4..)
                question_number += 1
            #checks if the users lives(chances) has reached 0
            if(lives <= 0):
                #The screen becomes red
                window.fill(blooming_red)
                #this text is displayed informing the user that they need to practice more
                display_text("You Failed! You need more review.", 900, 300, 100)
                run = False
                
            #If the variable question_index is less than the list of questions, then the game continues      
            if(question_index < len(list_of_questions) - 1):
                #index of the question is incremented
                question_index += 1
                #index of the answer is incremeneted
                list_ans_index += 1
            #If the previous statement is false, then the user has successfully answered all the questions without failing
            else:
                #The question on the screen becomes invisible
                question_on_screen = font3.render("", True, black)
                #invisible text is shown on screen
                window.blit(question_on_screen, (130, 120))
                #The background color becomes green
                window.fill(victory_green)
                #This text is displayed congratulating the user
                display_text("Congratulations! You have passed your practice test", 900, 300, 80)
                run = False

            
        #This processes all the events that the text box gets
        manager.process_events(event)
        
    
        
        
    

    #The textbox is updated at the refresh rate specified
    manager.update(refreshrate_ui)
    #The textbox is repeatedly draw on the window 
    manager.draw_ui(window)



    
    
      

    #The display is updated every time the loop runs     
    pygame.display.update()
    
#In the case that run = False in the loop, the program exits the loop and comes here, ending the program
pygame.quit()

















#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#Asset sources
#check mark downloaded from https://pngtree.com/freepng/green-check-mark-icon-design-template-vector_6219078.html 
#'x' mark downloaded from https://pngtree.com/freepng/red-x-fork_6001925.html

#import all the needed modules/libraries
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
font4 = pygame.font.SysFont("arialrounded", 40)

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
                   "(a)Another vehicle is in your way | (b) It may help prevent a collision | (c) Animal on road",
                   "(a)Stop and proceed cautiously | (b) Slowly pass vehicles that seem to be stopped | (c) Look to the sides of your vehicle to see what is coming",
                   "(a)A depressant | (b)A stimulant | (c)Both",
                   "(a)Farther from the car ahead than normal | (b)No different than normal | (c)Closer to the car ahead than normal",
                   "(a)Sound your horn | (b)Speed up to clear the area quickly | (c)Slow down and pass with caution",
                   "(a)Speed up | (b)Reduce your speed | (c)Drive at the posted speed",
                   "(a)Across from your vehicle | (b)Who arrived before you | (c)On your left",
                   "(a)During the first rain after a dry spell | (b)After it has been raining for awhile | (c)Heavy downpour"]


#Create the textbox UI
#parameters -> pygame_gui.elements.UITextEntryLine(rectangle, (length, height)), manager = what ever your manager is set to, object_id = "#name of the entry field")
text_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 500), (1750, 100)), manager = manager, object_id = "#text_box_entry")


#If user got a correct answer, the a check mark will be shown with 0 transparency(255) and then become transparent(0)
def correct_img(x, y):
    
    check_mark.set_alpha(255)
    #placed on screen
    window.blit(check_mark, (x, y))
    #transparency on
    check_mark.set_alpha(0)
    
    return


#If user got a incorrect answer, the an 'x' mark will be shown with 0 transparency(255) and then become transparent(0)
def incorrect_img(x, y): 
    #no transparency
    check_mark.set_alpha(255)
    #placed on screen
    window.blit(x_mark, (x, y))
    #transparency on
    x_mark.set_alpha(0)

    return

    


#This takes in a question and what the user responded with and checks if their answer matches with 
#the questions' corresponding answer in the dictionary
def check_correct(question, response):
    if(quest_ans[question].lower() == response.lower()):
        return True
   

#Displays text that the user enters at the specified location and with its font size
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


#Variable to store index of the question
question_index = 0
#The question side of the dictionary imported is converted to a list
list_of_questions = list(quest_ans.keys())
#lives/chances initialized
lives = 3
#variable that stores boolean value that will be used to control if the main loop will run or end
run = True
#variable to store the index of the answers shown on the screen
list_ans_index = 0
#stores the question number(ex. "1. What is the date")
question_number = 1

#main loop 
while run:
    
    #background color is set 
    window.fill(premium_gray)
    #Turquoise colored heading. Parameters = pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
    turq_rect = pygame.draw.rect(window, r_gray, (0,0, length, 75), 0)
    
    #Title of game created(1) then placed on screen(2)
    text_title = font1.render("Mock Driving Test", True, black)
    window.blit(text_title, (700, 15))

    #Text created to inform the user how to exit the program(1), text placed on screen(2)
    text_exit = font1.render("Esc = Exit", True, black)
    window.blit(text_exit, (1600, 15))

    #Text created to give a tip to the user(1), that text is placed on the screen(2)
    text_tip = font2.render("*Enter the letter corresponding to the answer choice* Enter only the letters a, b, or c or else it will count as incorrect!", True, black)
    window.blit(text_tip,(100, 600))
    



    #The refresh rate of the text box(the cursor blink)
    refreshrate_ui = clock.tick(60)/750 #The /750 controls how fast the cursor blinks(it slows it down)


    #The current question is stored in the variable and is decided by the question_index initialized outside the loop
    current_question = list_of_questions[question_index]

    #Text to show chances is created(1), that text is displayed on the screen(2)
    lives_display = font1.render("Chances: " + str(lives), True, black)
    window.blit(lives_display, (5, 15))

    #The text for the question shown on the screen is created
    question_on_screen = font_largest.render(str(question_number) + ". " + current_question, True, black)
    #The text for the answer choices on the screen is created
    answers_on_screen = font4.render(list_of_answers[list_ans_index], True, black)
    #The answer is placed on the screen
    window.blit(answers_on_screen, (70, 300))
    #The question is placed on the screen
    window.blit(question_on_screen, (70, 120))
    #The FPS variable is used to control the refresh rate of the loop
    clock.tick(FPS)
    
    #gets ever event that occurs(an event can be anything--button clicked--mouse clicked..etc)
    for event in pygame.event.get():
        #Program ends when 'x' pressed or exit is clicked
        if event.type == pygame.QUIT:
            run = False
        #if the user presses the escape key, the program will terminate
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        #checks if the user has clicked the text box AND entered a value
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#text_box_entry":
            #checks if their response is the correct answer to the question
            if(check_correct(current_question, event.text)):
                #A checkmark is shown on the screen
                correct_img(100, 100)
                #Makes the textbox empty(so previous answer is not shown for next question) 
                text_input.set_text("")
                #The question number is incremented by 1(question 1, 2, 3, 4..)
                question_number += 1

            #if their answer is incorrect
            else:
                #'x' mark is shown on the screen
                incorrect_img(100, 100)
                #Makes the textbox empty(so previous answer is not shown for next question)
                text_input.set_text("")
                #The lives(represents chances) is decremented by 1
                lives -= 1
                #The question number is incremented by 1(question 1, 2, 3, 4..)
                question_number += 1
            #checks if the users lives(chances) has reached 0
            if(lives <= 0):
                #The screen becomes red
                window.fill(blooming_red)
                #this text is displayed informing the user that they need to practice more
                display_text("You Failed! You need more review.", 900, 300, 100)
                run = False
                
            #If the variable question_index is less than the list of questions, then the game continues      
            if(question_index < len(list_of_questions) - 1):
                #index of the question is incremented
                question_index += 1
                #index of the answer is incremeneted
                list_ans_index += 1
            #If the previous statement is false, then the user has successfully answered all the questions without failing
            else:
                #The question on the screen becomes invisible
                question_on_screen = font3.render("", True, black)
                #invisible text is shown on screen
                window.blit(question_on_screen, (130, 120))
                #The background color becomes green
                window.fill(victory_green)
                #This text is displayed congratulating the user
                display_text("Congratulations! You have passed your practice test", 900, 300, 100)
                run = False

            
        #This processes all the events that the text box gets
        manager.process_events(event)
        
    
        
        
    

    #The textbox is updated at the refresh rate specified
    manager.update(refreshrate_ui)
    #The textbox is repeatedly draw on the window 
    manager.draw_ui(window)



    
    
      

    #The display is updated every time the loop runs     
    pygame.display.update()
    
#In the case that run = False in the loop, the program exits the loop and comes here, ending the program
pygame.quit()

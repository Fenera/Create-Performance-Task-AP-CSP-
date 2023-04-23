#Asset sources
#check mark(image) downloaded from https://pngtree.com/freepng/green-check-mark-icon-design-template-vector_6219078.html 
#'x' mark(image) downloaded from https://pngtree.com/freepng/red-x-fork_6001925.html

#import all the needed modules/libraries
import pygame
import pygame_gui
import time
import os

#Initialize the pygame module/library(1), Initializes the font class in pygame(2)
pygame.init()
pygame.font.init()

#This changes the directory of this python file to the file that it is being run out of(more portable from device to device)
#It allows me to easily load images in this file just by their name(ex: 'dog.png' instead of the actual direct-
# -ory of the image)
#The code one line below is a modified version from https://www.geeksforgeeks.org/python-os-path-abspath-method-with-example/
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Gets the dimensions/resolution of the screen the game is executed on
#ex. a screen with a resolution of 1920x1080 would be the stored in screen_information
screen_information = pygame.display.Info()


#length and height are set to the length and height of your screen(enables fullscreen usage)
#if 1920x1080 resolution then length = 1920 and height = 1080
length = screen_information.current_w
height = screen_information.current_h

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


#Creates window/the box that the user interacts with
window = pygame.display.set_mode((length,height), pygame.FULLSCREEN) #pygame.FULLSCREEN makes it full screen

#Set the caption of the window
pygame.display.set_caption("Practice Driving Exam")


#loads in two png images and scales them down for use in program
#(600, 600) --> 600x600
check_mark = pygame.image.load("check.png").convert_alpha()
check_mark = pygame.transform.scale(check_mark,(600, 600)) 
x_mark = pygame.image.load("incorrect.png").convert_alpha()
x_mark = pygame.transform.scale(x_mark, (600, 600))

#Initialize Fonts for later use using built-in font class in pygame
font1 = pygame.font.SysFont("arialrounded", 50)
font3 = pygame.font.SysFont("arialrounded", 30)
font2 = pygame.font.SysFont("arialrounded,", 20)
font4 = pygame.font.SysFont("arialrounded", 40)
font5 = pygame.font.SysFont("arialrounded", 65)
font_final = pygame.font.SysFont("arialrounded", 90)

#Creates a ui manager to manage all the events in text box
manager = pygame_gui.UIManager((length, height))

#create a FPS system so the game executes smoothely(Frames refreshed per second)
clock = pygame.time.Clock()
FPS = 60

#dictionary(list) that maps a question to its correct answer choice
#A key is the left hand item and the right hand item is known as a value
quest_ans = {"What does a flashing red light indicate?": "a",
             "What should you do if you encounter a flooded roadway?": "c",
             "What is the speed limit in business and residential areas?": "b",
             "If the rear end of your car starts skidding to the left, you should:" : "c",
             "When driving at night, you should: ": "a",
             "When driving in fog, rain, or snow, use:" : "b",
             "You should use your horn when: ": "b",
             "At intersections, crosswalks, and railroad crossings, you should always: " : "c",
             "If a road is slippery, maintain a following distance that is: " : "a",
             "You see pedestrians near the road. You should: " : "c",
             "If the roadway is wet or icy, you should: " : "b",
             "Roadways are the most slippery: " : "a"}

#This is a list of the answers that will be displayed on the screen
#They correlate to the questions in the quest_ans dictionary keys
list_of_answers = ["(a)Come to a complete stop | (b)Yield to oncoming traffic | (c)Drive through the intersection",
                   "(a)Drive through with caution | (b)Drive through quickly | (c)Do not attempt to drive through it",
                   "(a)30mph | (b)25mph | (c)20mph",
                   "(a)Steer right | (b)Keep steering wheel straight | (c) Steer left",
                   "(a)Increase following distance | (b)Use highbeams | (c) Decrease following distance",
                   "(a)High beams | (b)Low beams | (c)Only fog lights",
                   "(a)Another vehicle is in your way | (b) It may help prevent a collision | (c) Animal on road",
                   "(a)Stop and proceed cautiously | (b) Slowly pass vehicles that seem to be stopped | (c) Look to the sides of your vehicle",
                   "(a)Farther from the car ahead than normal | (b)No different than normal | (c)Closer to the car ahead than normal",
                   "(a)Sound your horn | (b)Speed up to clear the area quickly | (c)Slow down and pass with caution",
                   "(a)Speed up | (b)Reduce your speed | (c)Drive at the posted speed",
                   "(a)During the first rain after a dry spell | (b)After it has been raining for awhile | (c)Heavy downpour"]


#Create the textbox UI
#parameters -> pygame_gui.elements.UITextEntryLine(rectangle( so length & height), (location of box as (x, y))), manager = what ever your manager variable is called, object_id = "#name of the entry field(can be anything)")
text_input = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((80, 500), (1750, 100)), manager = manager, object_id = "#text_box_entry")


#Function if the user gets an incorrect answer 
#A check mark will be shown with no transparency(255) at location (x, y)
def correct_img(x, y):
    #transparency off
    check_mark.set_alpha(255)

    #placed on screen
    window.blit(check_mark, (x, y))
    return


#Function for when the user gets an incorrect answer
#An 'x' mark will be shown with no transparency(255) at location (x, y)
def incorrect_img(x, y): 
    #transparency off
    check_mark.set_alpha(255)

    #placed on screen
    window.blit(x_mark, (x, y))
    return

    


#*This takes in a question and what the user responded with(as parameters) and checks if their answer matches with 
# - the corresponding value in the dictionary
def check_correct(question, response):
    #quest_ans[question].lower() is what the correct answer is(ex: 'a', 'b', 'c')
    if(quest_ans[question].lower() == response.lower()):
        return True
   

#Displays text that the user enters at a specified location and with a specified font size
#(text_display = text to be displayed, x = horizontal coordinate, y = vertical coordinate, size = font size)
def display_text(text_display, x, y, size):
    while True:
        #Creates a font with the font size parameter
        #Text is rendered(created)
        #Creates a rectangle limit/boundary for the text with the center being x and y
        new_text = pygame.font.SysFont("arial", size).render(text_display, True, "black")
        new_text_rect = new_text.get_rect(center = (x ,y))

        #displays the rendered text where the rectangle is at
        window.blit(new_text, new_text_rect)
        
        #updates the window after text is loaded on screen
        pygame.display.update()


#Variable to store index of the question
question_index = 0

#The question side(key) of the dictionary is converted to a list
list_of_questions = list(quest_ans.keys())

#lives/chances initialized
lives = 3

#variable that stores boolean value that will be used to control if the main loop will run or end
run = True

#variable to store the index of the answers shown on the screen
list_ans_index = 0

#stores the question number(ex. "(1.) What is the date")
question_number = 1

#Boolean that will dictate wheter or not the game will end(used in main loop below)
end_the_game = False

#Increments every time the user gets a question correct
number_correct = 0

#main loop 
while run:

    #background color is set 
    window.fill(premium_gray)

    #Turquoise colored heading. Parameters = pygame.draw.rect(screen, [color as rgb], [left, top, length, height])
    turq_rect = pygame.draw.rect(window, r_gray, (0,0, length, 75))
    
    #Title of game created(1)
    text_title = font5.render("Mock Driving Test", True, black)
    #then text placed on screen(2)
    window.blit(text_title, (700, 26))

    #Text created to inform the user how to exit the program(1)
    text_exit = font5.render("Esc = Exit", True, black)
    #Then text placed on screen(2)
    window.blit(text_exit, (1600, 26))

    #Text created to give a warning to the user(1)
    text_tip = font3.render("*Enter the letter corresponding to the answer choice* Enter only the letters a, b, or c or else it will count as incorrect!", True, black)
    #That text is placed on the screen(2)
    window.blit(text_tip,(100, 600))
    
    #Text to show the user's chances is created(1)
    lives_display = font5.render("Chances: " + str(lives), True, black)

    #That text is displayed on the screen(2)
    window.blit(lives_display, (5, 26))



    #The refresh rate of the text box(for the cursor blink)
    refreshrate_ui = clock.tick(60)/750 #The /750 controls how fast the cursor blinks(it slows it down for higher numbers)


    #The current question is stored in the variable and is decided by the question_index initialized outside the loop
    current_question = list_of_questions[question_index]


    #The text for the question shown on the screen is created
    question_on_screen = font5.render(str(question_number) + ". " + current_question, True, black)

    #The text for the question is placed on the screen
    window.blit(question_on_screen, (70, 120))

    #The text for the answer choices is created
    answers_on_screen = font4.render(list_of_answers[list_ans_index], True, black)

    #The text for the answer choices is placed on the screen
    window.blit(answers_on_screen, (70, 300))
    
    #The FPS variable is used to control the refresh rate of the loop
    #I based my FPS counter on one from https://pythonprogramming.altervista.org/pygame-how-to-display-the-frame-rate-fps-on-the-screen/
    clock.tick(FPS)
    
    #Gets every event that occurs(an event can be anything--button clicked--mouse clicked--game ended..etc)
    for event in pygame.event.get():

        #Program terminates when 'x'(exit) is pressed
        if event.type == pygame.QUIT:
            run = False

        #if the user presses the escape key, the program will terminate
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        #checks if the user has clicked the text box AND entered a value
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#text_box_entry":

            #checks if their response is the correct answer to the question
            #event.text is the answer they entered
            if(check_correct(current_question, event.text)):
                #A checkmark is shown on the screen using the function correct_img(x,y)
                correct_img(100, 100)
                
                #This makes the textbox empty(so previous answer is not shown for next question) 
                text_input.set_text("")

                #The question number is incremented by 1(question 1, 2, 3, 4..)
                question_number += 1

                #increments number_correct since they got it correct
                number_correct += 1

                #index of the question is incremented
                question_index += 1

                #index of the answer is incremeneted
                list_ans_index += 1

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

                #index of the question is incremented
                question_index += 1

                #index of the answer is incremeneted
                list_ans_index += 1

        #checks if the users lives(chances) has reached 0(they failed)
        if(lives == 0):
            #The screen becomes red
            window.fill(blooming_red)

            #this text is displayed informing the user that they need to practice more
            display_text("You Failed! You need more review.", 950, 300, 80)

        
        #Checks if the user has gotten at least 9 questions correct and if they answered all the questions
        #9 because the most they can get wrong is 3(12 - 3 = 9)
        #question_number > 11 means that the user has answered all the questions(12)
        if(number_correct >= 9 and question_number > 11):
            end_the_game = True
            

        #If the variable end_the_game is true, then the user has successfully answered all the questions without failing(12 or more correct)
        if(end_the_game):
            #The background color becomes green
            window.fill(victory_green)

            #This text is displayed congratulating the user
            display_text("Congratulations! You have passed your practice test", 900, 300, 70)

        #This processes all the events that the text box gets
        manager.process_events(event)

    #The textbox is updated at the refresh rate specified
    manager.update(refreshrate_ui)

    #The textbox is repeatedly draw on the window(the parameter is the surface --> window)
    manager.draw_ui(window)

    #The display is updated every time the loop runs     
    pygame.display.update()





#**Outside loop**
#In the case that run = False in the loop, the program exits the loop and comes here, ending the program
pygame.quit()

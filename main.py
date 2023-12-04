import pygame
import requests
from pygame import mixer

pygame.init()
mixer.init()

#Load music file and set volume
mixer.music.load('lost-soul_medium-177571.mp3') #insert song here
mixer.music.set_volume(0.7)
mixer.music.play()
#bruh
def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
   
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

class GameState:
    MAIN_MENU = 0
    NAME_INPUT = 1
    GAMEPLAY = 2

current_state = GameState.MAIN_MENU

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)

volume_button_visible = True
start_exit_buttons_visible = True
#window set up
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("title of game") #replace with actual game title

#Font & text settings
font = pygame.font.Font(None, 36)
text_color = (255,255,255)

# font for start button - D
font_start = pygame.font.Font(None, 48)
game_name_text = font_start.render("Cracked and cackling", True , "white") # title subject to change - D
start_text = font_start.render("START", True , "black")
quit_text = font_start.render("QUIT", True , "black")

#Player name imput
input_box = pygame.Rect(335,500,140,32)
name = ""
input_active = True

#this the functtion to draw button
def draw_button():
    
    button_rect = pygame.Rect(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 50, 50, 30)
    pygame.draw.rect(window, (255, 0, 0), button_rect) #red button

    if start_exit_buttons_visible:
        # Display "What is your name?" text above the input box
        question_surface = font.render("What is your name?", True, (255, 255, 255))
        window.blit(question_surface, (input_box.x - 50, input_box.y - 50))

        start_button = pygame.Rect(300, 150, 200, 100)
        pygame.draw.rect(window, "white", start_button) #top white rectangle (start) - D
        window.blit(start_text, (345, 185)) #start text for the button - D

        quit_button = pygame.Rect(300, 300, 200, 100)
        pygame.draw.rect(window, "white", quit_button) #bottom white rectangle (quit) -D
        window.blit(quit_text, (355, 335)) #start text for the button - D

    window.blit(game_name_text, (220, 50))
display_text = False
display_time = 20000
display_start_time = 0

def display_start_text(player_name):
    text = (
        f"Dear {player_name}, \n"
        "Fate has led you to stumble across this old \n "
        "home. To avoid being cursed, you must \n"
        "explore 3 different rooms to escape. Once you \n "
        "enter a room, you will stumble upon different\n "
        "scenarios. You must make crucial choices \n"
        "that will impact your future or else… \n "
        "If you fail to escape, you will be trapped....\n "
        "Good Luck! \n"
        "Sincerely,\n"
        "    - Data Pirates\n"
    )

    box_width = 600
    box_height = 400
    box_x = (WINDOW_WIDTH - box_width) // 2
    box_y = (WINDOW_HEIGHT - box_height) // 2

    text_surface = font.render(text, True, text_color)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, text_color)
        window.blit(line_surface, (box_x + 20, box_y + 20 + i * 30))

    pygame.draw.rect(window, (255, 255, 255), (box_x, box_y, box_width, box_height), 3)

# For the first scenario
display_scenario1 = False
def display_first_scenario(player_name):
    text_scenario1 = (
        f"{player_name}, you have entered the \n" 
        "first room in the house, and you \n"
        "see a cup filled with an unusual \n"
        "substance, do you drink it? \n"
    )

    box2_width = 410
    box2_height = 150
    box_x = (WINDOW_WIDTH - box2_width) // 2
    box_y = (WINDOW_HEIGHT - box2_height) // 2

    lines = text_scenario1.split('\n')
    for i, line in enumerate(lines):
        line_surface = font.render(line, True, "white")
        window.blit(line_surface, (box_x + 20, box_y + 20 + i * 30))

    pygame.draw.rect(window, (255, 255, 255), (box_x, box_y, box2_width, box2_height), 3)

    # Define rectangles for Yes and No buttons
    yes_button = pygame.Rect(250, 400, 100, 50)
    no_button = pygame.Rect(450, 400, 100, 50)

    # Draw Yes button
    pygame.draw.rect(window, "green", yes_button)  # green button for Yes
    yes_text = font.render("Yes", True, "black")
    window.blit(yes_text, (280, 415))  # Adjust text position for Yes button

    # Draw No button
    pygame.draw.rect(window, "red", no_button)  # red button for No
    no_text = font.render("No", True, "black")
    window.blit(no_text, (480, 415))  # Adjust text position for No button

    return yes_button, no_button




volume_button = pygame.Rect(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 50, 50, 30)
running = True
name_input_done = False
player_name = ""
music_playing = True
start_button = pygame.Rect(300, 150, 200, 100)
quit_button = pygame.Rect(300, 300, 200, 100)

while running:
    window.fill(BLACK) #Fill the window with black
    draw_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if start_button.collidepoint(mouse_x, mouse_y) and not display_text:
                print("Start button clicked")
                
                if not name_input_done:
                    current_state = GameState.NAME_INPUT  # Switch to name input state
                

                    pygame.draw.rect(window, (255, 255, 255), input_box, 2)
                    text_surface = font.render(player_name, True, (255, 255, 255))
                    window.blit(text_surface, (input_box.x + 5, input_box.y + 5))

            if volume_button.collidepoint(mouse_x, mouse_y) and volume_button_visible:
                print("Volume button clicked")
                if music_playing:
                    mixer.music.pause()
                else:
                    mixer.music.unpause()  # Resume music playback
                music_playing = not music_playing
                pass

            if start_button.collidepoint(mouse_x, mouse_y) and not display_text:
                print("Start button clicked")
                if not name_input_done:
                    current_state = GameState.NAME_INPUT  # Switch to name input state
                else:
                    window.fill(BLACK)
                    display_text = True
                    display_scenario1 = True
                    display_start_time = pygame.time.get_ticks()
                    start_exit_buttons_visible = False

            elif quit_button.collidepoint(mouse_x, mouse_y) and not display_text:
                print("quit button clicked")
                pygame.quit()

        elif current_state == GameState.NAME_INPUT and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                name_input_done = True
                current_state = GameState.MAIN_MENU
            elif event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
            else:
                player_name += event.unicode

    if current_state == GameState.NAME_INPUT:
        pygame.draw.rect(window, (255, 255, 255), input_box, 2)
        text_surface = font.render(player_name, True, (255, 255, 255))
        window.blit(text_surface, (input_box.x + 5, input_box.y + 5))
         

    elif display_text:
        # Display start text with player's name after name input is done
        display_start_text(player_name if name_input_done else "Player")
        current_time = pygame.time.get_ticks()
        if current_time - display_start_time >= display_time:
            display_text = False 
    
    elif display_scenario1:
        # Displays the first scenario
        yes_button, no_button = display_first_scenario(player_name if name_input_done else "Player")

        # Check for button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if Yes button is clicked
            if yes_button.collidepoint(mouse_x, mouse_y):
                print("Yes button clicked")
                # Handle Yes action here

            # Check if No button is clicked
            if no_button.collidepoint(mouse_x, mouse_y):
                print("No button clicked")
                # Display the image
                image = pygame.image.load('Cup.png')  # Replace 'your_image.png' with your image file
                window.blit(image, (1, 1,))  # Adjust position as needed
                pygame.display.flip()

                # Play the audio
                audio = mixer.Sound('screams-of-agony-142447.mp3')  
                audio.play()

                
    pygame.display.flip()

pygame.quit()
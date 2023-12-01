import pygame
import requests
from pygame import mixer

pygame.init()
mixer.init()

#Load music file and set volume
mixer.music.load('lost-soul_medium-177571.mp3') #insert song here
mixer.music.set_volume(0.2)

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
   
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)

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
input_box = pygame.Rect(100,200,140,32)
name = ""
input_active = True

#this the functtion to draw button
def draw_button():
    button_rect = pygame.Rect(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 50, 50, 30)
    pygame.draw.rect(window, (255, 0, 0), button_rect) #red button

    start_button = pygame.Rect(300, 150, 200, 100)
    pygame.draw.rect(window, "white", start_button) #top white rectangle (start) - D
    window.blit(start_text, (345, 185)) #start text for the button - D

    quit_button = pygame.Rect(300, 300, 200, 100)
    pygame.draw.rect(window, "white", quit_button) #bottom white rectangle (quit) -D
    window.blit(quit_text, (355, 335)) #start text for the button - D

    window.blit(game_name_text, (220, 50))
display_text = False
display_time = 5000
display_start_time = 0

def display_start_text():
    text = (
        "Fate has led you to stumble across this old \n "
        "home.To avoid being cursed, you must \n"
        "explore 3 different rooms to escape Once you \n "
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


running = True

music_playing = False # to track music state
while running:
    window.fill(BLACK) #Fill the window with black
    draw_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_rect = pygame.Rect(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 50, 50, 30)
            start_button = pygame.Rect(300, 150, 200, 100)
            quit_button = pygame.Rect(300, 300, 200, 100)
            if button_rect.collidepoint(mouse_x, mouse_y):
                if music_playing:
                    mixer.music.pause()
                else:
                    mixer.music.unpause()
                music_playing = not music_playing

            elif start_button.collidepoint(mouse_x, mouse_y) and not display_text:
                print("Start button clicked")
                window.fill(BLACK)
                display_text = True
                display_start_time = pygame.time.get_ticks()

    if display_text:
        display_start_text()
        current_time = pygame.time.get_ticks()
        if current_time - display_start_time >= display_time:
            display_text = False   
                
    pygame.display.flip()

pygame.quit()
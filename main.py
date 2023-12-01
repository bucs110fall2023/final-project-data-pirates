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
        "Fate has led you to stumble across this old haunted mansion. "
        "To avoid being cursed, you must muster up the courage to go inside "
        "and explore 3 different rooms to escape and get away from the curses! "
        "Once you enter a room, you will stumble upon different scenarios "
        "in which you will have to use your intuition to make crucial choices "
        "that will impact your future or else… This could lead to dire consequences "
        "that you will regret! If you fail to escape, you will be trapped.... "
        "Good Luck! Sincerely, Data Pirates"
    )
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    pygame.draw.rect(window, (255, 255, 255), text_rect, 1)  # Outline around the text
    window.blit(text_surface, text_rect)
running = True

music_playing = False # to track music state
while running:
    window.fill(BLACK) #Fill the window with black
    draw_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #this gonna check if button clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_rect = pygame.Rect(WINDOW_WIDTH - 100, WINDOW_HEIGHT -50, 50, 30)
            start_button = pygame.Rect(300, 150, 200, 100) # D #D
            quit_button = pygame.Rect(300, 300, 200, 100) # D #D
            if button_rect.collidepoint(mouse_x, mouse_y):
                if music_playing:
                    mixer.music.pause()
                else:
                    mixer.music.unpause() #loops the music
                music_playing = not music_playing

            elif start_button.collidepoint(mouse_x, mouse_y) and not display_text: #D
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
import pygame
import requests

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)

def main():
    response = requests.get("https://youtu.be/9d9e6XmNn9Q?si=iqP9xeQUg1aplFxQ")
    print(response.status_code)
    print(response.text)
main()



#window set up
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("title of game") #replace with actual game title

#Font & text settings
font = pygame.font.Font(None, 36)
text_color = (255,255,255)

#Player name imput
input_box = pygame.Rect(100,200,140,32)
name = ""
input_active = True

#this the functtion to draw button
def draw_button():
    button_rect = pygame.Rect(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 50, 50, 30)
    pygame.draw.rect(window, (255, 0, 0), button_rect) #red button

running = True
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
            if button_rect.collidepoint(mouse_x, mouse_y):
                if music_playing:
                    main.stop()
                else:
                    main.play(-1) #loops the music
                music_playing = not music_playing

    pygame.display.flip()

pygame.quit()
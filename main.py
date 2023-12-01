import pygame
import requests
#import your controller

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

# font for start button - D
font_start = pygame.font.Font(None, 48)
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
    window.blit(quit_text, (360, 335)) #start text for the button - D

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
            start_button = pygame.Rect(300, 150, 200, 100) # D #D
            quit_button = pygame.Rect(300, 300, 200, 100) # D #D
            if button_rect.collidepoint(mouse_x, mouse_y):
                if music_playing:
                    main.stop()
                else:
                    main.play(-1) #loops the music
                music_playing = not music_playing

            if start_button.collidepoint(mouse_x, mouse_y): #D
                window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                window.fill("black")
                pygame.display.flip()
                pygame.time.wait(1000)

            if quit_button.collidepoint(mouse_x, mouse_y): #D
                main.stop()



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
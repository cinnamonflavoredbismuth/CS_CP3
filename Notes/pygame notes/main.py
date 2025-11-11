#CS Pygame Notes
"""
How do you set up pygame?
    pygame.init()
What is the purpose of the "While running" loop?
    so the program keeps running and doesn't close immediately
How do you create a screen in pygame?
    pygame.display.set_mode((1200, 720))
How are objects placed on the screen in pygame?
    screen.blit or screen.draw
What events can I listen for in pygame? What do those events do?
    exit, keypress, mouse click, mouse movement
How can I detect collision with pygame?
    
How do you add sounds in pygame?
    pygame.mixer.sound.play(pygame.mixer.Sound('soundfile.wav'))
"""
import pygame

pygame.init()

pygame.display.set_caption("Pygame Tutorial") #title of window
screen = pygame.display.set_mode((1200, 720)) #dimensions on screen
pos_x = 100
pos_y = 200

ufo = pygame.image.load("Notes/pygame notes/ufo.png") #load image file
#ufo = pygame.transform.scale(ufo, (100, 75)) #resize image
ufo_rect = ufo.get_rect(topleft = (558,558)) #get rectangle around image for collision detection

while True:
    screen.fill((128,0,128)) #background color RGB

    pygame.draw.rect(screen, (0,255,0), (100,200,50,75)) #draw rectangle (surface, color, (x,y,width,height))
    pygame.draw.circle(screen, (255,0,0), (400,300), 75) #draw circle (surface, color, (x,y), radius)
    pygame.draw.polygon(screen, (0,0,255), [(600,100),(700,200),(650,300),(550,300),(500,200)]) #draw polygon (surface, color, [(x1,y1),(x2,y2),...])

    screen.blit(ufo, (pos_x,pos_y)) #draw image on screen at (x,y)

    for event in pygame.event.get(): #as long as this is running, listen for things that happen, and do it if these happen
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        keys = pygame.key.get_pressed() #get list of all keys that are pressed
        if keys[pygame.K_LEFT]: #if left arrow key is pressed
            pos_x -= 50
        elif keys[pygame.K_RIGHT]: #if right arrow key is pressed
            pos_x += 50
        if keys[pygame.K_UP]: #if up arrow key is pressed
            pos_y -= 50
        elif keys[pygame.K_DOWN]: #if down arrow key is pressed
            pos_y += 50

    pygame.display.flip() #update display for next frame

def main():
    pass
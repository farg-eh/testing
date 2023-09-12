import pygame, sys
from button import Button

pygame.init()

screen = pygame.display.set_mode((0, 0))
SW, SH = screen.get_size()
clock = pygame.time.Clock()

btn = Button(pos=(SW/11, SH/20), name="Exit")

font = pygame.font.Font(None, 30)
screen_res = f"screen width : {SW}  screen height : {SH}"

while True:
    dt = clock.tick(60) / 1000
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if btn.check_click(pos) == "Exit":
                btn.surf.fill("red")  
                pygame.quit()
                sys.exit()
                
        if event.type == pygame.FINGERDOWN:
            screen.fill("brown")
            
        if event.type == pygame.FINGERUP:
            screen.fill("green")
            
        if event.type == pygame.FINGERMOTION:
            screen.fill("purple")
                
                
    # calculate fps
    fps = str(int(clock.get_fps()))
    
    # print text
    text= [screen_res, fps]
    pos = SW/9, SH - SH/3
    for i in range(len(text)):
        new_pos = pos[0], pos[1] + i*45        
        screen.blit(font.render(text[i],1,"red"), new_pos)
    
            
            
    # updating and drawing things
    btn.update(dt)
            
    pygame.display.update()
    
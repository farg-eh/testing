import pygame

class Button:
    def __init__(self, pos, name):
        self.screen = pygame.display.get_surface()
        self.pos = pos
        self.name = name
        self.size = (120, 90)
        
        self.surf = pygame.Surface(self.size)
        self.rect = self.surf.get_rect(center=pos)
        self.color = "white"
        pygame.draw.rect(self.surf,self.color,
        (0,0,self.size[0], self.size[1]), border_radius=30)
        # self.surf.fill(self.color)
        
        self.font = pygame.font.Font(None, 45)
        self.text = self.font.render(self.name, 1, "white")
        self.text_rect = self.text.get_rect(center=pos)
        
        
    def check_click(self, pos):
        x, y = self.pos
        w, h = self.surf.get_size()
        
        if x+w >= pos[0] >= x and y+h >= pos[1] >= y:
            return self.name
            
    
    def draw(self):
        self.screen.blit(self.surf, self.rect)
        self.screen.blit(self.text, self.text_rect)
        
        
        
    def update(self, dt):
        self.draw()
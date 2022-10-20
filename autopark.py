from cmath import *
from string import whitespace
import pygame


pygame.init()
game_over=False
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GRAY = (100,100,100)
display = pygame.display
screen = pygame.display.set_mode((1920,1030))

def rectRotated( surface, color, pos, fill, border_radius, angle ):
    """
    - angle in degree
    """
    max_area = max(pos[2],pos[3])
    s = pygame.Surface((max_area,max_area))
    s = s.convert_alpha()
    s.fill((0,0,0,0))
    pygame.draw.rect(s, color,(0,0,pos[2],pos[3]),fill, border_radius=border_radius)
    s = pygame.transform.rotate(s,angle)
    surface.blit( s, (pos[0],pos[1]) )      
    
class Player:
    def __init__(self,x,y,a,b,angle,speed):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.angle = angle
        self.speed = speed
    def forward(self):
        x+= self.speed * float(cos(self.angle))
        y+= self.speed * float(sin(self.angle))
    def draw(self):
        rectRotated(screen,WHITE,(self.x,self.y,self.a,self.b),0,15,self.angle)
player = Player(500,400,100,40,0,1)
while not game_over:
    events = pygame.event.get()
    for ev in events:
        if ev.type==pygame.QUIT:
            pygame.quit()
            game_over = True
        if ev.type == pygame.K_w:
            player.forward()
    player.draw()
    pygame.display.update()
import math
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
        self.x+= self.speed * float(math.sin((self.angle+90)*(math.pi/180)))
        self.y+= self.speed * float(math.cos((self.angle+90)*(math.pi/180)))
    def draw(self):
        rectRotated(screen,WHITE,(int(self.x),int(self.y),self.a,self.b),0,15,self.angle)
    def rotatep(self):
        self.angle +=0.1
    def rotaten(self):
        self.angle -=0.1
    def backward(self):
        self.x -= self.speed * float(math.sin((self.angle+90)*(math.pi/180)))
        self.y -= self.speed * float(math.cos((self.angle+90)*(math.pi/180)))
player = Player(500,400,100,40,0,0.1)
while not game_over:
    events = pygame.event.get()
    for ev in events:
        if ev.type==pygame.QUIT:
            pygame.quit()
            game_over = True
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                game_over = True
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_w]:
        player.forward()
        if keys[pygame.K_a]:
            player.rotatep()
        if keys[pygame.K_d]:
            player.rotaten()
    if keys[pygame.K_s]:
        player.backward()
        if keys[pygame.K_a]:
            player.rotaten()
        if keys[pygame.K_d]:
            player.rotatep()
    screen.fill(BLACK)
    player.draw()
    pygame.display.update()
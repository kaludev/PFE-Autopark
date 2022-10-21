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
clock = pygame.time.Clock()

def rectRotated( surface, color, pos, fill, border_radius, angle ):
    """
    - angle in degree
    """
    max_area = max(pos[2],pos[3])
    s = pygame.Surface((max_area,max_area))
    s = s.convert_alpha()
    s.fill((0,0,0,0))
    pygame.draw.rect(s, color,(0,0,pos[2],pos[3]),fill, border_radius=border_radius)
    offset = pygame.math.Vector2(25,30)
    s,p,center = rotate(s,angle,(pos[0],pos[1]),offset)
    #pygame.draw.circle(screen,GREEN,center=center,radius=4)
    surface.blit( s,p )    

def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(-angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    center=pivot+rotated_offset
    rect = rotated_image.get_rect(center=center)
    return rotated_image, rect,center  # Return the rotated image and shifted rect.

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
        self.angle +=2.5
    def rotaten(self):
        self.angle -=2.5
    def backward(self):
        self.x -= self.speed * float(math.sin((self.angle+90)*(math.pi/180)))
        self.y -= self.speed * float(math.cos((self.angle+90)*(math.pi/180)))
player = Player(500,400,100,40,0,5)
while not game_over:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_LSHIFT]:
        player.speed = 10
    else:
        player.speed = 5 
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
    #pygame.draw.circle(screen,GREEN,center=(player.x,player.y),radius=4)
    clock.tick(30)
    pygame.display.update()
    for ev in events:
        if ev.type==pygame.QUIT:
            pygame.quit()
            game_over = True
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                game_over = True
    
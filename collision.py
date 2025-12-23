import pygame
import random

#Constants for easier adjustments
Screen_Width,Screen_Height=500,400
Movement_Speed=5
Font_Size=72

#Intialize Pygame
pygame.init()

#Load and transform the background image
background_image = pygame.transform.scale(pygame.image.load("bg.jpg"),
                                          (Screen_Width,Screen_Height))

#Load font once at the beginning
font=pygame.font.SysFont("Times New Roman",Font_Size)

class Sprite(pygame.sprite.Sprite):

    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface ([width,height])
        self.image.fill(pygame.Color('dodger blue'))#Background color of sprite
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()

        def move(self,x_change,y_change):
            self.rect.x=max(
                min(self.rect.x+x_change,Screen_Width- self.rect.width),0)
            self.rect.y=max(
                min(self.rect.y+y_change,Screen_Height-self.rect.height),0)
            

            #Set up
            screen=pygame.display.set_mode((Screen_Width,Screen_Height))
            pygame.display.set_caption("Sprite Collision")
            all_sprites = pygame.sprite.Group()

            #Create sprites
            sprite1=Sprite(pygame.Color('black'),20,30)
            sprite1.rect.x,sprite1.rect.y = random.randint
            (0, Screen_Width-sprite1.rect.width),random.randint(
                0,Screen_Height-sprite1.rect.height)
            all_sprites.add(sprite1)
            sprite2=Sprite(pygame.color('red'),20,30)
            sprite2.rect.x,sprite2.rect.y = random.randint
            (0, Screen_Width-sprite2.rect.width),random.randint(
                0,Screen_Height-sprite2.rect.height)
            all_sprites.add(sprite2)

            #Game loop control variables
            running,won=True,False
            clock = pygame.time.Clock()
            #Main game loop
            while running:
                for event in pygame.event.get():
                    if event.type==pygame.Quit or (event.type==pygame.KEYDOWN
                                                   and event.key==
                    pygame.K_x):
                        running=False
                    if not won:
                        keys=pygame.keys.get_pressed()
                        x_change=(keys[pygame.K_RIGHT]-keys[pygame.K_UP])
                    Movement_Speed
                    y_change=(keys[pygame.K_DOWN]-keys[pygame.K_UP])


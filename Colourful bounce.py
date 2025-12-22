import pygame
import random

#Initialise Pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT+2

#Define basic colors using pygame.Color
#Background colors
Blue = pygame.Color('blue')
Lightblue= pygame.Color('lightblue')
Darkblue= pygame.Color('darkblue')

#Sprite colors
Yellow=pygame.Color('yellow')
Magenta=pygame.Color('magenta')
Orange=pygame.Color('orange')
White=pygame.Color('white')

#Sprite class representing the moving object 
class Sprite(pygame.sprite.Sprite):

    #Constructor method
    def __init__(self,color,height,width):
        #Callto the parent class(Sprite) constructor
        super().__init__()
        #Create the sprite's surface with dimensions and color
        self.image=pygame.Surface((width,height))
        self.image.fill(color)
        #Get the sprite's rect defining its position and size
        self.rect = self.image.get_rect()
        #Set initial velocity with random direction
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]

        #Methodto update the sprite's position
        def update (self):
            #Move the sprite by its velocity
            self.rect.move_ip(self.velocity)
            #Flag to track if the sprite hits a boundary
            boundary_hit=False
            #Check for collision with left or right boundaries and reverse direction
            if self.rect.left<=0 or self.rect.right>=500:
                self.velocity[0]=-self.velocity[0]
                boundary_hit=True
            #Check for collision with top or bottom boundaries and revers direction
            if self.rect.top<=0 or self.rect.bottom>=400
            self.velocity[1]=-self.velocity[1]
            boundary_hit=True
            #If boundary was hit,post events to change colors
            if boundary_hit:
                pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

            #Method to change the sprite's color
            def change_color(self):
                self.image.fill(random.choice([Yellow,Magenta,Orange,White]))
            
            #Function to change the backgrounf color
            def change_background_color():
                global bg_color
                bg_color=random.choice([Blue,Lightblue,Darkblue])
            
            #Create a group to hold the sprite
            all_sprites_list=pygame.sprite.Group()
            #Instantiate the sprite
            sp1=Sprite(White,20,30)
            #Randomly position the sprite
            sp1.rect.x= random.randint(0,480)
            sp1.rect.y=random.randint(0.370)
            #Add the sprite to the group
            all_sprites_list.add(sp1)

            #Create the game window
            screen=pygame.display.set_mode((500,400))
            #Set the window title
            pygame.display.set_caption("Boundary Sprite")
            #Set the initial background color
            bg_color=Blue
            #Apply background color
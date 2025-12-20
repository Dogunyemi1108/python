#Import necessary libraries
import pygame
pygame.init()
white=(255,255,255)

#Clock
clock = pygame.time.Clock()

#Creating the disply surface object
#of specific dimension..e(X,Y).
display_surface = pygame.display.set_mode((500,500))

#set the pygame window name
pygame.display.set_caption('Image')

#creating a surface object, image is drwan on it
image = pygame.image.load('turtle.jpg')

#Set the size for the image
DEFAULT_IMAGE_SIZE = (200,200)

#Scale the image to your needed size
image=pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

#Set a default position 
DEFAULT_IMAGE_SIZE=(150,150)

#infinite loop
while True:
    display_surface.fill(white)
    display_surface.blitt(image, DEFAULT_IMAGE_SIZE)

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            #quit the program
            quit()
    #Part of event loop
    pygame.display.flip()
    clock.tick(30)
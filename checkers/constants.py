import pygame

#WIll have to change other things accordingly
WIDTH = 800

#change to cols
ROWS =  8


#CHANGE THE COLORS
BROWN = "#63462D"
TAN = "#A3866A" 
BLACK  = "#000000" 

#place marker (change)
BLUE = "#FF0000" #RED
GREY = (128,128,128)

BLANK = 0
#Size of each square
SQUARE_DIM = 100

#loading and resizing the image using pygame method (change around)
CROWN = pygame.transform.scale(pygame.image.load('images/crown1.png'), (44,25))

IMG_WIDTH = 44 // 2
IMG_HEIGHT = 25 //2

IMG_WIDTHS = 60// 2
IMG_HEIGHTS = 90//2

#loading star
STAR = pygame.transform.scale(pygame.image.load('images/star.png'), (60,45))

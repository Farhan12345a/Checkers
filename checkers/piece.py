from .constants import BROWN, STAR, TAN, GREY, SQUARE_DIM, CROWN, STAR, IMG_WIDTH, IMG_HEIGHT, IMG_WIDTHS, IMG_HEIGHTS
import pygame

class Piece:

    #change this to custom padding and outline!!*****
    PADDING = 13
    OUTLINE = 4

    def __init__(self,row,col,color):
        self.row = row
        self.col =col
        self.color = color
        #Every piece starts off not being king
        self.king = False
        self.x = 0
        self.y = 0
        self.new_pos()

        #calculate x/y position based on row and coloumn your in
        #find starting x/y position
        #method that changes row and column
    def new_pos(self):
        #want to be middle of the square
        #SQUARE_SIZE//2 = 50**
        self.x = SQUARE_DIM * self.col + 50
        self.y = SQUARE_DIM * self.row + 50

        #make the piece a king
    def make_king(self):
        self.king = True
        
    #draws actual piece itself
    def draw(self, win):
        #drawing a circle
        #radius of circle
        radius = 35

        #draw the outline
        #Drawing a circle inside of a circle (small circle inside of big circle)
        #*ALT*
        pygame.draw.circle(win, GREY, (self.x,self.y), 38)
        pygame.draw.circle(win, self.color, (self.x,self.y), radius)

        if self.king:
            win.blit(CROWN, (self.x - IMG_WIDTH , self.y - IMG_HEIGHT//2))
        else:
            #Putting image on pieces
            win.blit(STAR, (self.x - IMG_WIDTHS, self.y - IMG_HEIGHTS//2))
   
   
    def move(self, newRow, newCol):
        #updates row and col
        self.row = newRow
        self.col = newCol
        #tells us x,y postion of our piece
        self.new_pos()
   

                    


import pygame

#Importing constants
#can be done by init.py file
from checkers.constants import WIDTH, SQUARE_DIM, BROWN
from checkers.game import Game

#Set up display 
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption('Choosen Checkers')



#take position of mouse and tell us what row and column we're in
def get_row_col_from_mouse(pos):
    #tells based of position wht row and column we're in
    x, y = pos
    row = y // SQUARE_DIM
    col = x // SQUARE_DIM
    return row,col

#used to run game
def main():
    start = True
    #Defining clock (runs in constant frame rate). 
    clock = pygame.time.Clock()

    #creating board object
    #board = Board() ALT
    game = Game(WIN)

    # need to add piece object
    #board.move()

    #the event is running
    while start:
        #60 frame per second
        clock.tick(60)

        #add popup window of winner
        if game.winner() != None:
            print(game.winner())

        #basic event loop for pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               start = False
            
            #Pressing the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #moving piece to position we want
                #select piece and where we want to move piece
                #gets mouse position
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)

                #whenever we press something
                game.select(row,col)
        
        #pygame.display.update()
        game.update()

    #Exiting loop and quitting game
    pygame.quit()
       
    

main()
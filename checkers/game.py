#responsible for handling the actual game
#whos turn
#did we select piece
#drawing everything
#etc

#let us interface with board/pieces 
#Can be incorporated in checkers.py

import pygame

from .constants import BROWN, TAN, BLUE, SQUARE_DIM
from checkers.board import Board

#Handling the actual game
#Let us interface w board, pieces, and everything else

class Game:
    #win: window draw the game 
    def __init__(self,win):
        self.selected = None
        self.board = Board()
        self.turn = BROWN
        self.valid_moves = {}
        self.win = win
    
    #updating pygame display
    def update(self):
        self.board.draw(self.win)

        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    
    def winner(self):
        return self.board.winner()

    #resets the game
    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = BROWN
        self.valid_moves = {}


    #selecting row and col
    #tell us row/col selected, based on that. game will do that
    #move piece or change selected piece
    def select(self,row,col): 
        #if we selected something, lets try to move what we selected to the row and col
        #if we have something selected, already have it. trying to move selected piece to specifc row/col
        if self.selected:
            result = self._move(row,col)
            #try to select diff piece
            #if place is invalid, reset the selection. Reselect something else
            if result is not None:
                #try to select different piece
                self.selected = None
                self.select(row,col) #Call method again

        piece = self.board.get_piece(row,col)
        #not selecting a empty piece
        #whatever turn currently is
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            #selection was valid
            return True
        
        #selection wasn't valid
        return False

    def _move(self,row,col):
        piece = self.board.get_piece(row,col)

        #have selected something and piece selected is 0 [empty space]:
        #only moves to empty space
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            #then move piece to specific row and col
            #move currently selected piece to specfic row and col
            self.board.move(self.selected, row, col)

            #check if position moved to had piece skipped
            skipped = self.valid_moves[(row,col)]
            #change turn
            

            if skipped:
                self.board.remove(skipped)

            self.change_turn()            

        else:
            return False

        #if this works
        return True

        
    #function to draw valid moves
    #the blue dots
    def draw_valid_moves(self, moves):
        #draw squares for all valid moves
        #loops through all the keys of dictionary
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_DIM + SQUARE_DIM//2, row * SQUARE_DIM + SQUARE_DIM//2), 15)



    def change_turn(self):
        #getting rid of valid moves after turn
        self.valid_moves = {}
        if self.turn == BROWN:
            self.turn = TAN 
        else:
            self.turn = BROWN
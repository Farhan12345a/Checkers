#Represnt checker board

import pygame

from .constants import BLACK, ROWS, BROWN, SQUARE_DIM, TAN, BLANK
from .piece import Piece
class Board:
    def __init__(self):
        self.board = []
        #self.turn = 0

        #12 pieces each
        self.brown = 12
        self.tan = 12
        #kings
        self.bk = 0
        self.tk = 0
        #Actually creates board
        self.create_board()

    #give me a surface to draw the tan and brown squares on. checker board path
    #drawing the squares in a pattern
    def draw_squares(self,win):
        win.fill(BLACK)

        for row in range(ROWS):
            #draw checker board pattern
            #skipping every other square
            alt_row = row % 2
            for col in range(alt_row, ROWS ,2):
                #draw rec on window which is red
                #() width, height (REC ARGUMENT LOOK UP) (x,y, size of square, size of square)
                pygame.draw.rect(win, BROWN, (row * SQUARE_DIM ,col * SQUARE_DIM, 100 , 100 ))

    #delete piece from where it is and move position
    #move piece as well
    def move(self, piece, row, col):
        #pieces are swapping the values
        #from current position to where the piece is about to move
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        
        #when piece is moved, follows parameter: row and column
        piece.move(row,col)

        #makes piece a king if the piece gets to end of the board
        if row == 0 or row == 7 :
            piece.make_king()

            #update the red and white kings
            if piece.color == TAN:
                self.tk += 1
            else:
                self.bk += 1 


    #gets a piece for us w row/column defined
    def get_piece(self,myRow,myCol):
        return self.board[myRow][myCol]

    #create acutual internal representation. adding pieces 
    def create_board(self):
        #creating a bunch of pieces
        #spread out pieces, four in each row, 
        for row in range(ROWS):
            #have list tht represents wht each row has inside of it
            self.board.append([])
            for col in range(ROWS):
                #if current column we'reon is divisble by 2 is equal (row+ 1) then, draw red/white cube
                #drawing piece in every other spot
                #drawing in either even/odd columns
                draw = (row + 1) % 2
                if col % 2 == (draw):
                    #only have pieces in first 3 rows
                    if row <= 2:
                        self.board[row].append(Piece(row,col, TAN))
                    #bottom section
                    #no pieces in row 3 and 4
                    #add 0 instead
                    elif row >= 5:
                        self.board[row].append(Piece(row,col,BROWN)) 
                    else: 
                        self.board[row].append(BLANK)
                else:
                    #adds a 0 if your not adding a piece
                    self.board[row].append(BLANK)

        pass
    
    #actually draw the board method
    def draw(self,win):
        #drawing squares on window
        self.draw_squares(win)

        #looping through pieces and drawing them
        for row in range(ROWS):
            for col in range(ROWS):
                #loop  throu
                piece = self.board[row][col]
            
                if type(piece) == Piece:
                    piece.draw(win)

    def remove(self, pieces):
        #loop throu pieces and remove the ones we need to
        for piece in pieces:
            #loop throu all the pieces and remove the specific pieces (= 0)
            self.board[piece.row][piece.col] = 0
            
            if piece != 0:

                if piece.color == BROWN:
                    self.brown -= 1
                else:
                    self.tan -= 1

    #determining winner
    def winner(self):
        if self.brown <= 0:
            return TAN
        elif self.tan <= 0:
            return BROWN

        #NO ONE WON
        return None

    def get_valid_moves(self,piece):
        #store moves as key(places where there are valid moves)
        #as (row,col) : ex
        moves = {}

        #getting left/right diagonal
        #moving left one
        left = piece.col - 1
        #considering diagonals
        right = piece.col + 1
        row = piece.row

        #**moving up and down
        #check whether moving up or down based on the color
        if piece.color == BROWN or piece.king:
            #update moves dictionary, with whatever is returned
            #row - 1: if red moving up(moving upwards): check row above
            #max(row-3, -1): how far up are we looking. -1: stop at -1 (row 0). row-3: dont want to look further then 2 rows above then current position
            #left: where we start for column
            moves.update(self._traverse_left(row - 1, max(row-3, -1), -1, piece.color,left))

            moves.update(self._traverse_right(row - 1, max(row-3, -1), -1, piece.color,right))

        if piece.color == TAN or piece.king:
            #row + 1 instead: moving down
            moves.update(self._traverse_left(row + 1, min(row+3, ROWS), 1, piece.color,left))

            moves.update(self._traverse_right(row + 1, min(row+3, ROWS), 1, piece.color,right))
        
        #return dictionary moves
        return moves

    #looks at left diagonal
    #Parameters: step:to we go up or down (diagonal)
    #skipped: have we skipped any pieces. 
    #left: where are we starting (column)
    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = []

        #tells what row start, stopping at, and step
        for r in range(start, stop, step):
            #situation where looking outside of board
            if left < 0:
                break
            
            #kepping track of col we are on
            current = self.board[r][left]

            #current == 0: found empty square
            #current thing looking at, check
            #if we skipped a piece and last isnt defined. 
            #if next square we look at when we jump piece, we cant move there
            if current == 0:
                if skipped and not last:
                    #if we skipped over something and found blank square.
                    # and we dont have anything we can skip again. Cant move there!!
                    
                    break
                elif skipped:
                    #mves[(r,left)]
                    #situation we found valid move and skipped over something
                    #combine last checker we jumped with checker we jumped on this move
                    #know tht we can jump 1 or 2.
                    moves[(r,left)] = last + skipped
                else:
                    #added as possible move
                    #add move but dont skip anything
                    moves[(r, left)] = last

                #aka: skipped over something
                #if last had a value in it (after finding)
                #had something we skipped over, skip it, 
                #seeing if we can double/triple jump. what row to stop at
                #DOUBLE / TRIPLE JUMP !!!!!!!
                if last:
                    #What direction are we going (up or down)
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)

                    #call recursivly to see if we can double/triple jump again
                    #either going up or down based on step
                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))

                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))

                    #optional break
                break

            #if its not empty, and equal to our piece. Cant move there
            #wont be addding any other moves
            elif current.color == color:
                #not adding other moves
                break
            else:
                #it was the other color
                #could move over top, if its empty square next

                last = [current]



            left -= 1

        return moves
     

    #looks at right diagonal
    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        #tells what row start, stopping at, and step
        for r in range(start, stop, step):
            #situation where looking outside of board
            #make sense with COLS instead of ROWS
            if right >= ROWS:
                break
            
            #kepping track of col we are on
            current = self.board[r][right]

            #current == 0: found emptyh square
            #current thing looking at, check
            #if we skipped a piece and last isnt defined. 
            #if next square we look at when we jump piece, we cant move there
            if current == 0:
                if skipped and not last:
                    #if we skipped over something and found blank square.
                    # and we dont have anything we can skip again. Cant move there!!
                    break
                elif skipped:
                    #situation we found valid move and skipped over something
                    #combine last checker we jumped with checker we jumped on this move
                    #know tht we can jump 1 or 2.

                    moves[(r,right)] = last + skipped
                else:
                    #added as possible move
                    #add move but dont skip anything
                    moves[(r, right)] = last

                #aka: skipped over something
                #if last had a value in it (after finding)
                #had something we skipped over, skip it, 
                #seeing if we can double/triple jump. what row to stop at
                if last:
                    #What direction are we going (up or down)
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)

                    #call recursivly to see if we can double/triple jump again
                    #either going up or down based on step
                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))

                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))

                    #optional break
                break

            #if its not empty, and equal to our piece. Cant move there
            #wont be addding any other moves
            elif current.color == color:
                break
            else:
                #it was the other color
                #could move over top, if its empty square next

                last = [current]



            right += 1

        return moves


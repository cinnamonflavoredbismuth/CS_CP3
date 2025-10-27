#CS Chess Pieces
'''Follow the provided class diagram exactly 
Implement ChessPiece as an abstract class 
Create all six concrete piece classes (Pawn, Rook, Knight, Bishop, Queen, King) 
Implement canMoveTo(), getSymbol() methods 
Create ChessGame class with whitePieces and blackPieces lists 
Implement movePiece(), removePiece(), getPiecesLeft(), and getPieceAt() in ChessGame 
Create correct number of pieces for each player 
Set up pieces in starting positions 
Demonstrate moving 5 different pieces 
Implement basic move validation for each piece type 
Use removePiece() method for capturing 
Put each class in its own file 
Add comments to explain your code 
Test each piece type for correct movement 
Focus on core functionality over advanced game logic'''
from abc import ABC, abstractmethod

board=[ ['','','','','','','',''], # 0
        ['','a','b','c','d','e','f','g','h'], # 1
        ['','a','b','c','d','e','f','g','h'], # 2
        ['','a','b','c','d','e','f','g','h'], # 3
        ['','a','b','c','d','e','f','g','h'], # 4
        ['','a','b','c','d','e','f','g','h'], # 5
        ['','a','b','c','d','e','f','g','h'], # 6
        ['','a','b','c','d','e','f','g','h'], # 7
        ['','a','b','c','d','e','f','g','h']  # 8
       ]
#print(board[0])



class ChessPiece:
    def __init__(self,color='',letter=0,number=0,board=[
        ['','','','','','','',''], # 0
        ['','a','b','c','d','e','f','g','h'], # 1
        ['','a','b','c','d','e','f','g','h'], # 2
        ['','a','b','c','d','e','f','g','h'], # 3
        ['','a','b','c','d','e','f','g','h'], # 4
        ['','a','b','c','d','e','f','g','h'], # 5
        ['','a','b','c','d','e','f','g','h'], # 6
        ['','a','b','c','d','e','f','g','h'], # 7
        ['','a','b','c','d','e','f','g','h']  # 8
    ]):
        self.color=color
        self.letter = letter
        self.number = number
        self._board=board
        
        self.position=self._board[number][letter]

    def try_except(self,a,b):

        try:
            board[a][b]
            return True
        except:
            return False
        
    def getPosition(self):
        return self.position
    
        

    @abstractmethod
    def canMoveTo(self,NewPos=''):
        pass
    @abstractmethod
    def getSymbol(self):
        pass
    
class Pawn(ChessPiece):
    def __init__(self, color='', letter=0,number=0):
        super().__init__(color, letter,number)

    def canMoveTo(self,NewPos):
        if self.color == 'white':
            canGo=[self._board[self.number-1][self.letter]]
        elif self.color == 'white':
             canGo=[self._board[self.number+1][self.letter]]
        else: canGo=[self._board[0][0]]

        if NewPos in canGo:
            return True
        else: return False

    def getSymbol(self):
        if self.color == 'white':
            return 'wp'
        elif self.color == 'black':
            return 'bp'
        else: return 'p'
    
class Rook(ChessPiece):
    def __init__(self, color='', letter=0,number=0):
        super().__init__(color, letter,number)
        
    def canMoveTo(self,NewPos):

        canGo=[]
        for x in range(8):
            if self.try_except(self.number+x,self.letter) != False:
                canGo.append(self._board[self.number+x][self.letter])
        for x in range(8):
            if self.try_except(self.number,self.letter+x) != False:
                canGo.append(self._board[self.number][self.letter+x])

        if NewPos in canGo:
            return True
        else: return False

    def getSymbol(self):
        if self.color == 'white':
            return 'wr'
        elif self.color == 'black':
            return 'br'
        else: return 'r'

class Knight(ChessPiece):
    def __init__(self, color='', letter=0,number=0):
        super().__init__(color, letter,number)

    def canMoveTo(self,NewPos):
        canGo=[]
        board=[[self.number-2,self.letter-1],[self.number-2,self.letter+1],[self.number+2,self.letter-1],[self.number+2,self.letter+1],[self.number-1,self.letter-2],[self.number-1,self.letter-2],[self.number-1,self.letter+2],[self.number+1,self.letter-2],[self.number+1,self.letter-2],[self.number+1,self.letter+2]]
        for x in board:
            if self.try_except(x[0],x[1]) != False:
                    canGo.append(self._board[x[0]][x[1]])

        if NewPos in canGo:
            return True
        else: return False

    def getSymbol(self):
        if self.color == 'white':
            return 'wk'
        elif self.color == 'black':
            return 'bk'
        else: return 'k'

class Bishop(ChessPiece):
    def __init__(self, color='', letter=0,number=0):
        super().__init__(color, letter,number)
        
    def canMoveTo(self,NewPos):
        canGo=[]
        for x in range(8):
            if self.try_except(self.number+x,self.letter+x) != False: canGo.append(self._board[self.number+x][self.letter+x])
        for x in range(8):
            if self.try_except(self.number-x,self.letter+x) != False: canGo.append(self._board[self.number-x][self.letter+x])
        for x in range(8):
            if self.try_except(self.number+x,self.letter-x) != False: canGo.append(self._board[self.number+x][self.letter-x])
        for x in range(8):
            if self.try_except(self.number-x,self.letter-x) != False: canGo.append(self._board[self.number-x][self.letter-x])

        if NewPos in canGo:
            return True
        else: return False

    def getSymbol(self):
        if self.color == 'white':
            return 'wb'
        elif self.color == 'black':
            return 'bb'
        else: return 'b'

class Queen(ChessPiece):
    def __init__(self, color='', letter=0,number=0):
        super().__init__(color, letter,number)
        
    def canMoveTo(self,NewPos):
        canGo=[]
        for x in range(8):
            if self.try_except(self.number+x,self.letter+x) != False: canGo.append(self._board[self.number+x][self.letter+x])
        for x in range(8):
            if self.try_except(self.number-x,self.letter+x) != False: canGo.append(self._board[self.number-x][self.letter+x])
        for x in range(8):
            if self.try_except(self.number+x,self.letter-x) != False: canGo.append(self._board[self.number+x][self.letter-x])
        for x in range(8):
            if self.try_except(self.number-x,self.letter-x) != False: canGo.append(self._board[self.number-x][self.letter-x])
        for x in range(8):
            if self.try_except(self.number,x) != False: canGo.append(self._board[self.number][x])
        for x in range(8):
            if self.try_except(x,self.letter) != False:canGo.append(self._board[x][self.letter])

        if NewPos in canGo:
            return True
        else: return False

    def getSymbol(self):
        if self.color == 'white':
            return 'wq'
        elif self.color == 'black':
            return 'bq'
        else: return 'q'
        
class King(ChessPiece):
    def __init__(self, color='', letter=0,number=0):
        super().__init__(color, letter,number)
        
    def canMoveTo(self,NewPos):
        canGo=[]
        if self.try_except(self.number+1,self.letter+1) != False: canGo.append(self._board[self.number+1][self.letter+1])
    
        if self.try_except(self.number-1,self.letter+1) != False: canGo.append(self._board[self.number-1][self.letter+1])
    
        if self.try_except(self.number+1,self.letter-1) != False:   canGo.append(self._board[self.number+1][self.letter-1])
    
        if self.try_except(self.number-1,self.letter-1) != False: canGo.append(self._board[self.number-1][self.letter-1])
    
        if self.try_except(self.number,self.letter+1) != False: canGo.append(self._board[self.number][self.letter+1])
    
        if self.try_except(self.number+1,self.letter1) != False:    canGo.append(self._board[self.number+1][self.letter])

        if self.try_except(self.number,self.letter-1) != False: canGo.append(self._board[self.number][self.letter-1])
    
        if self.try_except(self.number-1,self.letter) != False: canGo.append(self._board[self.number-1][self.letter])
    

        if NewPos in canGo:
            return True
        else: return False

    def getSymbol(self):
        if self.color == 'white':
            return 'wq'
        elif self.color == 'black':
            return 'bq'
        else: return 'q'
#'''
class ChessGame:
    def __init__(self,
    whitePieces=[Rook('white',1,1),Knight('white',2,1),Bishop('white',3,1),Queen('white',4,1),King('white',5,1),Bishop('white',6,1),Knight('white',7,1),Rook('white',8,1),Pawn('white',1,2),Pawn('white',2,2),Pawn('white',3,2),Pawn('white',4,2),Pawn('white',5,2),Pawn('white',6,2),Pawn('white',7,2),Pawn('white',8,2)],
    blackPieces=[Rook('black',1,8),Knight('black',2,8),Bishop('black',3,8),Queen('black',4,8),King('black',5,8),Bishop('black',6,8),Knight('black',7,8),Rook('black',8,8),Pawn('black',1,7),Pawn('black',2,7),Pawn('black',3,7),Pawn('black',4,7),Pawn('black',5,7),Pawn('black',6,7),Pawn('black',7,7),Pawn('black',8,7)]
    ):
        self.whitePieces=whitePieces
        self.blackPieces=blackPieces
    def removePiece(self,piece=ChessPiece()):
        piece.position=piece._board[0][0]
        return
    def movePiece(self,piece=ChessPiece(),NewPos=board[0][0]):
        if piece.canMoveTo(NewPos) == True:
            for x in self.blackPieces:
                if x.position == NewPos:
                    print(f"{piece.color} piece captured {x.color}'s {x.getSymbol()}")
                    self.removePiece(x)
            for x in self.whitePieces:
                if x.position == NewPos:
                    print(f"{piece.color} piece captured {x.color}'s {x.getSymbol()}")
                    self.removePiece(x)
            piece.position = NewPos
            return
        else:
            print('You can not move there')
            return
        
    def getPiecesLeft(self,color):
        if color == 'white':
            pieces=self.whitePieces
        elif color == 'black':
            pieces=self.blackPieces
        else: pieces=[]
        for x in pieces:
            if x.position == x._board[0][0]:
                pass
            else:
                print(x.getSymbol())
        else:
            return 0
        
    def getPieceAt(self,position=board[0][0]):
        for x in self.whitePieces:
            if x.position == position:
                print(f'At {position} is white {x.getSymbol()}')
                return
        for x in self.blackPieces:
            if x.position == position:
                print(f'At {position} is black {x.getSymbol()}')
                return
        print(f'At {position} is no piece')
        return
    





game=ChessGame()
game.movePiece(game.whitePieces[0],board[4][1])
game.movePiece(game.blackPieces[1],board[3][2])
game.movePiece(game.whitePieces[2],board[5][3])
game.movePiece(game.whitePieces[3],board[4][4])
game.movePiece(game.blackPieces[4],board[4][4])
print(f'{game.whitePieces[3].getSymbol()} is at {game.whitePieces[3].position}')
game.getPieceAt(board[3][2])
game.removePiece(game.blackPieces[1])
game.getPiecesLeft('black')

#'''

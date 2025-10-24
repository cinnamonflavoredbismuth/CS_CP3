#CS Chess Pieces
from abc import ABC, abstractmethod

board=[ [],
        ['','a','b','c','d','e','f','g','h'], # 1
        ['','a','b','c','d','e','f','g','h'], # 2
        ['','a','b','c','d','e','f','g','h'], # 3
        ['','a','b','c','d','e','f','g','h'], # 4
        ['','a','b','c','d','e','f','g','h'], # 5
        ['','a','b','c','d','e','f','g','h'], # 6
        ['','a','b','c','d','e','f','g','h'], # 7
        ['','a','b','c','d','e','f','g','h']  # 8
       ]

class ChessPiece:
    def __init__(self,color='',letter=0,number=0,board=[ 
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
        self.position=board[number][letter]
        self._board=board
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
            canGo.append(self._board[self.number][x])
        for x in range(8):
            canGo.append(self._board[x][self.letter])

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
        canGo.append(self._board[self.number-2][self.letter-1])
        canGo.append(self._board[self.number-2][self.letter+1])
        canGo.append(self._board[self.number+2][self.letter-1])
        canGo.append(self._board[self.number+2][self.letter+1])

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
            canGo.append(self._board[self.number+x][self.letter+x])
        for x in range(8):
            canGo.append(self._board[self.number-x][self.letter+x])
        for x in range(8):
            canGo.append(self._board[self.number+x][self.letter-x])
        for x in range(8):
            canGo.append(self._board[self.number-x][self.letter-x])

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
            canGo.append(self._board[self.number+x][self.letter+x])
        for x in range(8):
            canGo.append(self._board[self.number-x][self.letter+x])
        for x in range(8):
            canGo.append(self._board[self.number+x][self.letter-x])
        for x in range(8):
            canGo.append(self._board[self.number-x][self.letter-x])
        for x in range(8):
            canGo.append(self._board[self.number][x])
        for x in range(8):
            canGo.append(self._board[x][self.letter])

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
        canGo.append(self._board[self.number+1][self.letter+1])
    
        canGo.append(self._board[self.number-1][self.letter+1])
    
        canGo.append(self._board[self.number+1][self.letter-1])
    
        canGo.append(self._board[self.number-1][self.letter-1])
    
        canGo.append(self._board[self.number][self.letter+1])
    
        canGo.append(self._board[self.number+1][self.letter])

        canGo.append(self._board[self.number][self.letter-1])
    
        canGo.append(self._board[self.number-1][self.letter])

        if NewPos in canGo:
            return True
        else: return False

    def getSymbol(self):
        if self.color == 'white':
            return 'wq'
        elif self.color == 'black':
            return 'bq'
        else: return 'q'

class ChessGame:
    def __init__(self,whitePieces=[],blackPieces=[]):
        self.whitePieces=whitePieces
        self.blackPieces=blackPieces
    def movePiece(self,piece=ChessPiece(),NewPos=''):
        if piece.canMoveTo(NewPos) == True:
            for x in self.blackPieces:
                if x.position == NewPos:
                    print('You can not move there')
                    return
            for x in self.whitePieces:
                if x.position == NewPos:
                    print('You can not move there')
                    return
            piece.position = NewPos
            return
        else:
            print('You can not move there')
            return
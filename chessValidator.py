
# Possible pieces on a chessboard
chessPieces = ['wpawn', 'bpawn', 'wbishop', 'bbishop', 'wknight', 'bknight', 'wrook', 'brook', 'wqueen', 'bqueen', 'wking', 'bking']

# Possible number of pieces on a chessboard
chessboardValidPieces = {
    'wpawn': 8,
    'bpawn': 8,
    'wbishop': 2,
    'bbishop': 2,
    'wknight': 2,
    'bknight': 2,
    'wrook': 2,
    'brook': 2,
    'wqueen': 1,
    'bqueen': 1,
    'wking': 1,
    'bking': 1,

}

# Actual chessboard and pieces on it
chessBoard = {'1h': 'bking',
              '2h': 'wbishop', 
              '3h': 'wbishop', 
              '4h': 'wbishop', 
              '5h': 'wbishop', 
              '6h': 'wbishop', 
              '7h': 'wbishop', 
              '8h': 'wbishop', 
              '3a': 'wbishop', 
              '3b': 'wbishop', 
              '3c': 'wbishop', 
              '3d': 'wbishop', 
              '3f': 'wbishop', 
              '3g': 'wbishop', 
              '3j': 'wbishop', 
             '6c': 'wqueen',
             '2g': 'bbishop',
             '2a': 'bbishop', 
             '2b': 'wbishop', 
             '2c': 'wbishop', 
             '2d': 'wbishop', 
             '2e': 'bbishop', 
             '2j': 'qbishop', 
             '5h': 'bqueen',
             '3e': 'wking'}

# Check the total number of pieces on a chessboard. It should be less than or equal to 32
def isValidNumberPieces(chessBoard):
    return len(chessBoard) <= 32

# Count pieces on a chessboard by its color and name 
def countPieces(chessBoard):
    count = {}
    for v in chessBoard.values():
        count[v] = count.get(v, 0) + 1
    return count

# Count pieces on a chessboard by their color
def countPiecesByColor(chessBoard):
    count = {}
    for v in chessBoard.values():
        count[(v[0])] = count.get(v[0], 0) + 1
    return count

# Check chessboard for its validity
def isValidChessBoard(dict):
    # Check chessboard has valid number of pieces
    if (isValidNumberPieces(dict)):
        print('Chessboard has valid number of pieces')
    else:
        print('Chessboard has not valid number of pieces')
        print('Chessboard is not valid !!!')
        return
    
    count = countPieces(dict)
    # Check a chessboard must have one and only white king on it
    if (count['wking'] == chessboardValidPieces['wking']):
        print('Chessboard has one white king')
    else:
        print('Cheassboard must have one and only white king. You have',count['wking'], 'white king(s) on your chessboard')
        print('Chessboard is not valid !!!')
        return
    
    # Check a chessboard must have one and only black king on it
    if (count['bking'] == chessboardValidPieces['bking']):
        print('Chessboard has one black king')
    else:
        print('Cheassboard must have one and onlye black king. You have', count['bking'], 'black king(s) on your chessboard')
        print('Chessboard is not valid !!!')
        return

    # Check white and black pieces: each color cannot be more than 16 things
    whiteAndBlackPieces = countPiecesByColor(dict)
    if (whiteAndBlackPieces['w'] > 16):
        print('It is not allowed to have more than 16 white pieces on a chessboard. You have', whiteAndBlackPieces['w'], 'white pieces on the chessboard')
        print('Chessboard is not valid !!!')
        return

    if (whiteAndBlackPieces['b'] > 16):
        print('It is not allowed to have more than 16 black pieces on a chessboard. You have', whiteAndBlackPieces['b'], 'black pieces on the chessboard')
        print('Chessboard is not valid !!!')
        return

    print('Chessboard is valid!!!')
    #countByPieceAndColor = countPieces(dict)


isValidChessBoard(chessBoard)
print(countPiecesByColor(chessBoard))
#print(countPieces(chessBoard))
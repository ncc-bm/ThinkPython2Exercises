
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
            #   '4h': 'wbishop', 
            #   '5h': 'wbishop', 
            #   '6h': 'wbishop', 
            #   '7h': 'wbishop', 
            #   '8h': 'wbishop', 
            #   '3a': 'wbishop', 
            #   '3b': 'wbishop', 
            #   '3c': 'wbishop', 
            #   '3d': 'wbishop', 
            #   '3f': 'bbishop', 
              '3g': 'bbishop', 
              '3h': 'bbishop', 
             '6c': 'wqueen',
             '2g': 'bbishop',
             '2a': 'bbishop', 
             '2b': 'wbishop', 
             '2c': 'wbishop', 
             '2d': 'wbishop', 
            #  '2e': 'bbishop', 
             '2h': 'wbishop', 
             '5h': 'bqueen',
             '4a': 'wpawn',
             '4b': 'wpwwn',
             '4c': 'wpawn',
             '4d': 'wpawn',
             '4e': 'wpawn',
             '4f': 'bpawn',
             '4g': 'bpawn',
             '4h': 'bpawn',
            #  '4i': 'bpawn',
            #  '4k': 'bpawn',
             '8e': 'wking'}

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
        print('Chess board has valid number of pieces')
    else:
        print('Chess board has not valid number of pieces. You have more than 32 pieces on the chess board' )
        print('Chess board is not valid !!!')
        return

    whiteAndBlackPieces = countPiecesByColor(dict)

    # Check that all pieces start with letter 'w' or 'b'
    # dictionary whiteAndBlackPieces contains how many in total black and white pieces on the chess board
    # whiteAndBlackPieces should contain only two keys (w and b)
    if (len(whiteAndBlackPieces.keys()) > 2):
        print('There can be only two types of chess pieces: black and white. You have', len(whiteAndBlackPieces.keys()), 'kind of (color) chess pieces on the board')
        print('Chess board is not valid !!!')
        return
    elif ('w' not in whiteAndBlackPieces.keys()):
        print('There is no white pieces on the chess board')
        print('Chess board is not valid !!!')
        return
    elif ('b' not in whiteAndBlackPieces.keys()):
        print('There is no black pieces on the chess board')
        print('Chess board is not valid !!!')
        return
    else:
        print('Chessboard has valid white and black pieces on the board')
    
    count = countPieces(dict)
    # Check a chessboard must have one and only white king on it
    if (count['wking'] == chessboardValidPieces['wking']):
        print('Chess board has one white king')
    else:
        print('Cheass board must have one and only white king. You have',count['wking'], 'white king(s) on your chess board')
        print('Chess board is not valid !!!')
        return
    
    # Check a chessboard must have one and only black king on it
    if (count['bking'] == chessboardValidPieces['bking']):
        print('Chess board has one black king')
    else:
        print('Cheass board must have one and onlye black king. You have', count['bking'], 'black king(s) on your chess board')
        print('Chess board is not valid !!!')
        return

    # Check white and black pieces: each color cannot be more than 16 things
    if (whiteAndBlackPieces['w'] > 16):
        print('It is not allowed to have more than 16 white pieces on a chessboard. You have', whiteAndBlackPieces['w'], 'white pieces on the chess board')
        print('Chess board is not valid !!!')
        return
    else:
        print('The chess board has a valid number',whiteAndBlackPieces['w'], '(not more than 16) of white pieces.')

    if (whiteAndBlackPieces['b'] > 16):
        print('It is not allowed to have more than 16 black pieces on a chessboard. You have', whiteAndBlackPieces['b'], 'black pieces on the chess board')
        print('Chess board is not valid !!!')
        return
    else:
        print('The chess board has a valid number',whiteAndBlackPieces['b'], '(not more than 16) of black pieces.')

    if (count.get('wpawn', 0) > chessboardValidPieces['wpawn']):
        print('There should be no more than 8 white pawns in a chess board. You have', count['wpawn'], 'white pawns in the chess board.')
        print('Chess board is not valid !!!')
        return
    else:
        print('The chess board has a valid number', count.get('wpawn', 0), '(not more than 8) of white pawns')

    if (count.get('bpawn', 0) > chessboardValidPieces['bpawn']):
        print('There should be no more than 8 black pawns in a chess board. You have', count['bpawn'], 'black pawns in the chess board.')
        print('Chess board is not valid !!!')
        return
    else:
        print('The chess board has a valid number', count.get('bpawn', 0), '(not more than 8) of black pawns')
    
    # Check chess pieces located within a valid space from 1a to 8h
    for k, v in dict.items():
        # There cannot be more than two symbols in a piece location
        if (len(k) != 2): 
            print('Chess board piece', v, 'located in not valid space', k)
            print('Chess board is not valid !!!')
            return
        # First symbol of the piece location should be number between 1 to 8 (range(1,9) gives this range)
        elif (int(k[0]) not in range(1,9)):
            print('Chess board piece', v, 'located in not valid space', k)
            print('Chess board is not valid !!!')
            return
        # The second symbol of the piece location should be letter from a to h
        elif (str(k[1]) not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')):
            print('Chess board piece', v, 'located in not valid space', k)
            print('Chess board is not valid !!!')
            return
    
    # if the previous check passed, it can be considered that all chess pieces located within a valid space
    print('All chess pieces located within valid space (from 1a to 8h)')

    # Check chess board have pieces with valid piece names:
    for v in chessBoard.values():
        if (v not in chessPieces):
            print('Chessboard has a piecse', v, 'with invalid name')
            print('Chess board is not valid !!!')
            return
    
    print('Chessboard has pieces with valid names')
            

    print('Chess board is valid!!!')
    #countByPieceAndColor = countPieces(dict)


isValidChessBoard(chessBoard)
#print(countPiecesByColor(chessBoard))
#print(countPieces(chessBoard))
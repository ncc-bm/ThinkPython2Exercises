chessValidPieces = {
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
chessBoard = {'1h': 'bking',
             '6c': 'wqueen',
             '2g': 'bbishop',
             '5h': 'bqueen',
             '3e': 'wking'}

def isValidNumberPieces(dict):
    return len(dict) <= 32

#def countFigures(dict):


def isValidChessBoard(dict):
    for k, v in dict.values():
        print(k)
    #print(list(dict.keys()))
    #print('wking' in dict.values())
    print(isValidNumberPieces(dict))
    

isValidChessBoard(chessBoard)